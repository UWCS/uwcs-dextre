import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
BOWER_COMPONENTS_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, "../components"))

COMPRESS_PRECOMPILERS = (
    ('text/x-scss',
     'sass --style compressed'
     ' -I "%s/bower_components/foundation-sites/scss"'
     ' -I "%s/bower_components/bulma"'
     ' -I "%s/bower_components/motion-ui"'
     ' {infile} "{outfile}"' % (BOWER_COMPONENTS_ROOT, BOWER_COMPONENTS_ROOT, BOWER_COMPONENTS_ROOT)),
)
