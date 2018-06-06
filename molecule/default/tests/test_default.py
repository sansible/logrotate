import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    assert host.package('logrotate').is_installed


def test_files(host):
    for config in ['application_logs', 'test_three']:
        assert host.file('/etc/logrotate.d/%s' % config).is_file


def test_configs(host):
    for config in ['application_logs', 'test_three']:
        cmd = host.run('logrotate -d /etc/logrotate.d/%s' % config)
        assert 'error:' not in cmd.stderr
