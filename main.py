from os import path, listdir
from docx import Document as docx_Document
from pymupdf import Document as pdf_Document

from lexer import Lexer
from model import TermFreq


def index_document(doc_content: str) -> TermFreq:
    tf: TermFreq = dict()
    lexer = Lexer(doc_content)
    for token in lexer:
        term = "".join(token).upper()
        if term in tf:
            tf[term] += 1
        else:
            tf[term] = 1
    return tf


def parse_pdf(doc_name: str) -> str:
    with open(doc_name, 'rb') as f:
        return "".join([page.get_text() for page in pdf_Document(f)])


def parse_docx(doc_name: str) -> str:
    with open(doc_name, 'rb') as f:
        return "\n".join([i.text for i in docx_Document(f).paragraphs])


def read_doc(doc_name: str) -> str | None:
    extension = path.splitext(doc_name)[-1]
    try:
        match extension:
            case ".docx":
                return parse_docx(doc_name)
            case '.pdf':
                return parse_pdf(doc_name)
            case _:
                return None
    except PermissionError as e:
        print(e)
        return None


def main() -> None:
    tf_index: dict[str, TermFreq] = dict()

    for doc in listdir("."):
        doc_content = read_doc(doc)
        if doc_content:
            print(f"Indexing \"{doc}\"")
            tf_index[doc] = index_document(doc_content)

    for doc in tf_index:
        print(f"\"{doc}\" has {len(tf_index[doc])} unique tokens")


if __name__ == "__main__":
    main()
