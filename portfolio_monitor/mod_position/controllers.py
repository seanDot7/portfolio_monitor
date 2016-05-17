# -*- coding: utf-8 -*-
from flask import Blueprint, abort, request, jsonify
from ..services import data_service

mod_position = Blueprint('position', __name__, url_prefix='/positions')

#  @mod_position.route('/', methods=['GET'])
#  def modPositionTest():
    #  return '[mod_position] test'

@mod_position.route('', methods=['GET'])
def getPosition():
    if request.args.get('accountId') and request.args.get('date'):
        accountId = request.args.get('accountId')
        date = request.args.get('date')
        data = None
        if request.args.get('stats'):
            data = jsonify(data_service.getStats(accountId, date))
        else:
            data = data_service.getCsvData(accountId, date)

        if data != None:
            return data
    else:
        abort(400)
