import nox


@nox.session(
    python=[
        '3.5',
        '3.6',
        '3.7',
    ],
)
def tests(session):
    session.install('.')
    session.run('python', 'setup.py', 'test')
