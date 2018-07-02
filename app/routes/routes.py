from . import sp
from flask import render_template


@sp.route('/')
def main():
    return render_template('main.html')