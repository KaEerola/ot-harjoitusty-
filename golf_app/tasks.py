from invoke import task

@task
def start(ctx):
    ctx.run("python -m src.main", pty=True)

@task
def test(ctx):
    ctx.run("python -m unittest discover -s src/tests", pty=True)

@task
def coverage_report(ctx):
    ctx.run("coverage run -m unittest discover -s src/tests", pty=True)
    ctx.run("coverage html", pty=True)
