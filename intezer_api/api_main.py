#!/usr/bin/env python
from http import HTTPStatus
from flask import Flask, request, jsonify
from intezer_api.managers.index_doc_manager import index_single_document, index_documents
import requests
import flask


app = Flask('api')

SEARCH_SERVICE_URL = "http://127.0.0.1:8000/"


@app.route('/index/url')
def index_words_from_url():
    url = request.args.get('url')
    req = requests.get(url).json()
    index_documents(req)
    return flask.make_response('Pass', HTTPStatus.OK)


@app.route('/index/document', methods=['POST'])
def index_words_from_document():
    req_data = request.get_json()
    index_single_document(req_data)
    return flask.make_response('Pass', HTTPStatus.OK)


@app.route('/document/get-by-sentence')
def get_document_by_sentence():
    sentence = request.args.get('sentence')
    sensitive = request.args.get('sensitive')
    params = {'sentence': sentence, "sensitive": sensitive}
    response = requests.get(url=SEARCH_SERVICE_URL + "/document/get-by-sentence", params=params).json()
    sorted_response = str({k: v for k, v in sorted(response.items(), key=lambda item: item[1]['score'], reverse=True)})
    return flask.make_response(jsonify(sorted_response), HTTPStatus.OK)


@app.route('/documents/get-by-phrase')
def get_document_by_phrase():
    phrase = request.args.get('phrase')
    sensitive = request.args.get('sensitive')
    params = {'phrase': phrase, "sensitive": sensitive}
    response = requests.get(url=SEARCH_SERVICE_URL + "/documents/get-by-phrase", params=params).json()
    return flask.make_response(jsonify(response), HTTPStatus.OK)


if __name__ == '__main__':
    app.run(port=5000)
