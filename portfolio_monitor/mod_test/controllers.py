# -*- coding: utf-8 -*-
from flask import Blueprint

mod_test = Blueprint('test', __name__, url_prefix='/test')

@mod_test.route('/hello/', methods=['GET'])
def hello():
    return '[mod_test] hello!'

