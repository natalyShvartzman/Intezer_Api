from intezer_api.rabbitmq import sender


def index_documents(docs: dict):
    [index_single_document(doc) for doc in docs["documents"]]


def index_single_document(doc: dict):
    sender.send('document', 'localhost', doc)
