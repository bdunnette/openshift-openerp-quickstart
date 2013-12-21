from setuptools import setup

setup(name='YourAppName', version='1.0',
      description='OpenShift Python-2.7 Community Cartridge based application',
      author='Your Name', author_email='ramr@example.org',
      url='http://www.python.org/sigs/distutils-sig/',
      dependency_links = ['http://download.gna.org/pychart/'],

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['gevent',
                        #'CherryPy',
                        #'MySQL-python',
                        #'pymongo',
                        #'psycopg2',

                        # OpenERP requires
                        'pychart',
                        'babel',
                        'docutils',
                        'feedparser',
                        'gdata',
                        'Jinja2',
                        'lxml',
                        'mako',
                        'mock',
                        # We use Pillow instead PIL
                        'pillow',
                        # PIL must be installed using pip, not easy_install.
                        # See https://mail.python.org/pipermail/image-sig/2010-August/006480.html
                        #'PIL', # windows binary http://www.lfd.uci.edu/~gohlke/pythonlibs/
                        'psutil', # windows binary code.google.com/p/psutil/downloads/list
                        'psycopg2 >= 2.2',
                        'pydot',
                        'python-dateutil < 2',
                        #'python-ldap', # optional
                        'python-openid',
                        'pytz',
                        'pywebdav',
                        'pyyaml',
                        'reportlab', # windows binary pypi.python.org/pypi/reportlab
                        'simplejson',
                        'unittest2',
                        'vatnumber',
                        'vobject',
                        'werkzeug',
                        'xlwt',
      ],
     )
