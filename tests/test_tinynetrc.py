import pytest
import tinynetrc
import os

HERE = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def netrc():
    return tinynetrc.Netrc(os.path.join(HERE, '.netrc'))


def test_file_not_found():
    with pytest.raises(IOError):
        tinynetrc.Netrc('notfound')


def test_file_not_found_create(tmp_path):
    path = os.path.join(tmp_path, 'notfound')
    with tinynetrc.Netrc(path, create=True) as netrc:
        pass
    assert os.path.exists(path)


def test_home_unset(monkeypatch):
    # Make "~" == the current directory
    monkeypatch.setattr(os.path, 'expanduser', lambda path: HERE)
    # Unset $HOME
    monkeypatch.delenv('HOME', raising=False)
    # No error
    result = tinynetrc.Netrc()
    assert 'mail.google.com' in result.hosts


def test_hosts(netrc):
    assert 'mail.google.com' in netrc.hosts
    assert isinstance(netrc.hosts['mail.google.com'], tuple)


def test_machines(netrc):
    assert 'mail.google.com' in netrc.machines
    assert isinstance(netrc.machines['mail.google.com'], dict)
    assert netrc.machines['mail.google.com']['login'] == 'joe@gmail.com'
    assert netrc.machines['mail.google.com']['account'] == 'justagmail'
    assert netrc.machines['mail.google.com']['password'] == 'somethingSecret'


def test_dict_like_behavior(netrc):
    assert 'mail.google.com' in netrc
    assert netrc['mail.google.com']['login'] == 'joe@gmail.com'
    assert len(netrc) == len(netrc.machines)
    assert list(netrc) == list(netrc.machines)
    del netrc['mail.google.com']
    assert 'mail.google.com' not in netrc.machines


def test_machine_formatting(netrc):
    assert 'login joe@gmail.com' in netrc.format()


def test_machines_can_be_modified(netrc):
    netrc.machines['mail.google.com']['password'] = 'newpassword'
    assert 'newpassword' in netrc.format()


def test_machines_can_be_added(netrc):
    netrc.machines['api.heroku.com']['login'] = 'joe@test.test'
    netrc.machines['api.heroku.com']['password'] = 'supersecret'
    assert 'api.heroku.com' in netrc.format()
    assert 'supersecret' in netrc.format()


def test_machines_can_be_removed(netrc):
    assert 'mail.google.com' in netrc.format()
    del netrc.machines['mail.google.com']
    assert 'mail.google.com' not in netrc.format()

def test_is_dirty_after_addition(netrc):
    assert netrc.is_dirty is False
    netrc.machines['api.heroku.com']['login'] = 'joe@test.test'
    assert netrc.is_dirty is True

def test_is_dirty_after_deletion(netrc):
    assert netrc.is_dirty is False
    del netrc['mail.google.com']
    assert netrc.is_dirty is True
