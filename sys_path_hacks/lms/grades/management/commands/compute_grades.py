from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'grades.management.commands.compute_grades')

from lms.djangoapps.grades.management.commands.compute_grades import *
