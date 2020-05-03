from intezer_api.rabbitMQ.sender import send


def index_docs(docs):
    [index_single_doc(doc) for doc in docs["documents"]]


def index_single_doc(doc):
    send('docs', 'localhost', doc)
