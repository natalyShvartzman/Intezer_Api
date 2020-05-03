from flask import Flask, request
import requests

from intezer_api.managers.index_doc_manager import index_single_doc, index_docs

app = Flask('api')

SEARCH_SERVICE_URL = "http://127.0.0.1:8000/"


@app.route('/indexWordsFromUrl')
def index_words_from_url():
    url = request.args.get('url')
    req = requests.get(url).json()
    index_docs(req)


@app.route('/indexWordsFromDoc', methods=['POST'])
def index_words_from_doc():
    req_data = request.get_json()
    index_single_doc(req_data)


@app.route('/getDocumentBySentence')
def get_document_by_sentence():
    sentence = request.args.get('sentence')
    sensitive = request.args.get('sensitive')
    params = {'sentence': sentence, "sensitive": sensitive}
    response = requests.get(url=SEARCH_SERVICE_URL + "/getDocumentBySentence", params=params).json()
    return str({k: v for k, v in sorted(response.items(), key=lambda item: len(item[1]), reverse=True)})


@app.route('/getDocumentByPhrase')
def get_document_by_phrase():
    phrase = request.args.get('phrase')
    sensitive = request.args.get('sensitive')
    params = {'phrase': phrase, "sensitive": sensitive}
    response = requests.get(url=SEARCH_SERVICE_URL + "/getDocumentByPhrase", params=params).json()
    return str({k: v for k, v in sorted(response.items(), key=lambda item: len(item[1]), reverse=True)})


if __name__ == '__main__':
    app.run(port=5000)
