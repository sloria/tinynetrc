# -*- coding: utf-8 -*-
"""Read and write .netrc files."""
import netrc
import os
from collections import defaultdict

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

__version__ = '1.3.1'


def dictify_hosts(hosts):
    ret = defaultdict(lambda: {
        'login': None,
        'account': None,
        'password': None,
    })
    for machine, info in hosts.items():
        ret[machine] = {
            'login': info[0],
            'account': info[1],
            'password': info[2],
        }
    return ret


def dedictify_machines(machines):
    return {
        machine: (info.get('login'), info.get('account'), info.get('password'))
        for machine, info
        in machines.items()
    }


class Netrc(MutableMapping):

    def __init__(self, file=None):
        if file is None:
            file = os.path.join(os.path.expanduser('~'), '.netrc')
        self.file = file
        self._netrc = netrc.netrc(file)
        self.machines = dictify_hosts(self._netrc.hosts)

    def authenticators(self, host):
        return self._netrc.authenticators(host)

    @property
    def hosts(self):
        return self._netrc.hosts

    ##### dict-like interface implementation #####

    def __getitem__(self, key):
        return self.machines[key]

    def __setitem__(self, key, value):
        self.machines[key] = value

    def __delitem__(self, key):
        del self.machines[key]

    def __iter__(self):
        return iter(self.machines)

    def __len__(self):
        return len(self.machines)

    #### end dict-like interface implementation #####

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if not exc_type and self.is_dirty:
            self.save()

    def __repr__(self):
        return repr(dict(self.machines))

    @property
    def is_dirty(self):
        return self.machines != dictify_hosts(self._netrc.hosts)

    # Adapted from https://github.com/python/cpython/blob/master/Lib/netrc.py
    # to support Python 2
    def format(self):
        """Dump the class data in the format of a .netrc file."""
        self._netrc.hosts = dedictify_machines(self.machines)
        rep = ""
        for host in self._netrc.hosts.keys():
            attrs = self._netrc.hosts[host]
            rep += "machine {host}\n\tlogin {attrs[0]}\n".format(host=host,
                                                                 attrs=attrs)
            if attrs[1]:
                rep += "\taccount {attrs[1]}\n".format(attrs=attrs)
            rep += "\tpassword {attrs[2]}\n".format(attrs=attrs)
        for macro in self._netrc.macros.keys():
            rep += "macdef {macro}\n".format(macro=macro)
            for line in self._netrc.macros[macro]:
                rep += line
            rep += "\n"
        return rep

    def save(self):
        with open(self.file, 'w') as fp:
            fp.write(self.format())
