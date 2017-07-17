from distutils.core import setup

setup(name='docker_bash',
      version='0.1',
      description='Executes `bash` or `psql` on running Docker processes.',
      author='Jon Hill',
      author_email='jon@jonhill.ca',
      url='https://github.com/jonhillmtl/docker-bash',
      license='MIT',
      entry_points={
          'console_scripts': [
              'docker-bash=docker_bash:docker_bash',
              'docker-psql=docker_bash:docker_psql',
          ],
      },
      packages=['docker_bash'],
      install_requires=['termcolor']
)
