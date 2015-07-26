"""An OpenStack library.

Parsing configuration options from the command
line and configuration files.
"""

# http://www.giantflyingsaucer.com/blog/?p=4822
# pip install oslo.config
""" configuration example  - app.conf
[simple]
enable = True
[morestuff]
# StrOpt
message = Hello World
# ListOpt
usernames = tungnt, nttung, ungntt
# DictOpt
usermetadata = {'Joe': 'Manager', 'Jessica': 'CEO', 'Peter': 'Security Guard'}
# IntOpt
payday = 20
# FloatOpt
pi = 3.14
"""

from oslo_config import cfg

# define section in configuration files
opt_simple_group = cfg.OptGroup(name='simple',
                                title='A simple example')
opt_morestuff_group = cfg.OptGroup(name='morestuff',
                                   title='A more complex example')
simple_opts = [
    cfg.BoolOpt('enable', default=False,
                help=('True enables, False disables'))
]

morestuff_opts = [
    cfg.StrOpt('message', default='No data',
               help=('A message')),
    cfg.ListOpt('usernames', default=None,
                help=('A list of usernames')),
    cfg.DictOpt('usermetadata', default=None,
                help=('a dict of name and job title')),
    cfg.IntOpt('payday', default=30,
               help=('Default payday monthly date')),
    cfg.FloatOpt('pi', default=0.0,
                 help=('The value of Pi'))
]

CONF = cfg.CONF

CONF.register_group(opt_simple_group)
CONF.register_opts(simple_opts, opt_simple_group)

CONF.register_group(opt_morestuff_group)
CONF.register_opts(morestuff_opts, opt_morestuff_group)

if __name__ == '__main__':
    CONF(default_config_files=['app.conf'])
    print "morestuff - usernames: %s" % CONF.morestuff.usernames[1]
    print "morestuff - jobtitle: %s" % CONF.morestuff.usermetadata
