"""simple script parse command line argument and .ini configurations files."""

# http://www.giantflyingsaucer.com/blog/?p=4822
# pip install oslo.config
# imprort oslo config

from oslo.config import cfg

# define section in configuration file
opt_group = cfg.OptGroup(name='simple',
                         title='A simple example')

simple_opts = [
    cfg.BoolOpt('enable', default=False,
                help=('True enables, False disables'))
]

CONF = cfg.CONF
