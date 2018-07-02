from . import sp


@sp.route('/')
def hello_world():
    return 'Hello World!'