import nox


@nox.session
def tests(session):
    session.install('.')
    session.install('pytest')
    session.run('pytest', 'tests.py')


@nox.session
def lint(session):
    session.install('flake8')
    session.run('flake8', 'gitsnapshot.py', 'tests.py')
