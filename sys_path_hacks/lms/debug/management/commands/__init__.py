from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'debug.management.commands')

from lms.djangoapps.debug.management.commands import *
