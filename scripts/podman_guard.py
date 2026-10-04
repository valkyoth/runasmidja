"""Host-side rootless boundary shared by services, public builds and probes."""
import os


def require_rootless(run_command, *, local=False, env=None):
    if os.getuid() == 0 or os.geteuid() == 0:
        raise RuntimeError('Podman workflows refuse execution as root')
    options = ['--remote=false'] if local else []
    # Inspect the same connection/environment as the operation. Never cache.
    result = run_command('podman', *options, 'info', '--format',
                         '{{.Host.Security.Rootless}}', **({'env': env} if env is not None else {}))
    if result.stdout.strip() != 'true':
        raise RuntimeError('A rootless Podman engine is required')


def podman(run_command, *arguments, **kwargs):
    # Engine selection uses the shared environment, not unchecked global flags.
    if not arguments or arguments[0].startswith('-'):
        raise ValueError('Podman wrapper requires a subcommand')
    require_rootless(run_command, env=kwargs.get('env'))
    return run_command('podman', *arguments, **kwargs)


def archive(run_command, save_archive, image, target):
    require_rootless(run_command)
    return save_archive(['podman', 'save', '--format', 'docker-archive', image], target)


def unshare(run_command, supervisor, worker, **kwargs):
    # This must run on the host, before namespace UID 0 becomes legitimate.
    require_rootless(run_command, local=True, env=kwargs.get('env'))
    return run_command(*supervisor, 'podman', '--remote=false', 'unshare', 'unshare',
                       '--mount', '--propagation', 'private', *worker, **kwargs)
