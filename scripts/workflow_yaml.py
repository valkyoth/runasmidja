"""Bounded, deliberately restricted YAML reader for workflow policy, not execution."""
from pathlib import Path

try:
    import yaml
except ImportError as error:
    raise RuntimeError('Run scripts/install_python_tools.sh and use .local/check-tools/bin/python3') from error

VERSION = '6.0.3'
MAX_BYTES = 128 * 1024
MAX_EVENTS = 20_000
MAX_TOKENS = 40_000
MAX_DEPTH = 40


def load(path):
    """Read regular UTF-8 YAML; preserve all scalars as strings, including `on`."""
    if yaml.__version__ != VERSION:
        raise ValueError('workflow policy requires the reviewed PyYAML version ' + VERSION)
    with Path(path).open('rb') as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError('YAML exceeds byte limit')
    source = raw.decode('utf-8')
    # Unknown directives are silently ignored by the upstream parser; inspect
    # tokens as well so all directives reject, without matching ordinary strings.
    for count, token in enumerate(yaml.scan(source, Loader=yaml.BaseLoader), 1):
        if count > MAX_TOKENS:
            raise ValueError('YAML exceeds token limit')
        if isinstance(token, yaml.tokens.DirectiveToken):
            raise ValueError('YAML directives are not admitted')
    depth = 0
    for count, event in enumerate(yaml.parse(source, Loader=yaml.BaseLoader), 1):
        if count > MAX_EVENTS:
            raise ValueError('YAML exceeds event limit')
        if isinstance(event, yaml.events.AliasEvent) or getattr(event, 'anchor', None):
            raise ValueError('YAML anchors and aliases are not admitted')
        if getattr(event, 'tag', None) is not None:
            raise ValueError('explicit YAML tags are not admitted')
        if isinstance(event, yaml.events.DocumentStartEvent) and (event.version or event.tags):
            raise ValueError('YAML directives are not admitted')
        if isinstance(event, yaml.events.CollectionStartEvent):
            depth += 1
            if depth > MAX_DEPTH:
                raise ValueError('YAML exceeds depth limit')
        elif isinstance(event, yaml.events.CollectionEndEvent):
            depth -= 1
    # Compose nodes, never construct Python objects from YAML tags.
    node = yaml.compose(source, Loader=yaml.BaseLoader)

    def convert(item):
        if isinstance(item, yaml.ScalarNode):
            return item.value
        if isinstance(item, yaml.SequenceNode):
            return [convert(value) for value in item.value]
        if not isinstance(item, yaml.MappingNode):
            raise ValueError('expected YAML document')
        result = {}
        for key, value in item.value:
            if not isinstance(key, yaml.ScalarNode):
                raise ValueError('mapping keys must be scalar strings')
            if key.value in result or key.value == '<<':
                raise ValueError('duplicate or merge YAML key')
            result[key.value] = convert(value)
        return result

    try:
        return convert(node)
    except RecursionError as error:
        raise ValueError('YAML nesting rejected') from error
