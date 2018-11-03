"""
Link Management Routes
"""
import functools
import random
from src.cache import get_cache
from flask import Blueprint, redirect, request, current_app as app, json, jsonify

bp = Blueprint('api', __name__)

@bp.route('/health')
def health():
    msg = jsonify({'message': 'healthy'})
    return msg, 200

@bp.route('/roulette', methods=['GET'])
def roulette():
    r = get_cache()
    keys = r.get('roulette')
    if (keys is None):
        msg = jsonify({'message': 'No links for roulette'})
        return msg, 404
    else:
        key = random.sample(keys,1)[0]
        value = r.get(key) 
        dump = request_to_dict(request)
        r.sadd(key + ":client", dump)
        return redirect(value, code=302)

@bp.route('/<key>', methods=['GET'])
def forward(key):
    r = get_cache()
    
    if (r.exists(key)) :
        value = r.get(key) 
        dump = request_to_dict(request)
        r.sadd(key + ":client", dump)
        return redirect(value, code=302)
    else :
        msg = jsonify({'message': 'Link not found'})
        return msg, 404

@bp.route('/<key>', methods=['POST'])
def create(key):
    r = get_cache()
    if (r.exists(key)):
        msg = jsonify({'message': 'Link with key ' + key + ' already exists'})
        return msg, 502
    else:
        payload = request.get_json(force = True) 
        dump = request_to_dict(request)
        if 'roulette' in payload:
            r.set('roulette', key)
        r.set(key, payload['url'])
        r.hmset(key + ":founder", dump)
        msg = jsonify({'message': 'Link Created'})
        return msg, 201

@bp.route('/<key>', methods=['PUT'])
def override(key):
    r = get_cache()
    if (r.exists(key)):
        payload = request.get_json(force = True) 
        dump = request_to_dict(request)
        if 'roulette' in payload:
            r.set('roulette', key)
        r.set(key, payload['url'])
        r.hmset(key + ":founder", dump)
        msg = jsonify({'message': 'Link Updated'})
        return msg, 201
    else:
        msg = jsonify({'message': 'Nothing to override with key ' + key})
        return msg, 502


def request_to_dict(request):
    """
    Transform request into usable metadata
    """
    dump = {}
    dump['X-Founder-Ip'] = request.remote_addr
    for k,v in request.headers.to_list():
        dump[k] = v
    return dump
            