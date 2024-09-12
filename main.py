from os import path, listdir
from docx import Document as docx_Document
from pymupdf import Document as pdf_Document

from lexer import Lexer


def index_document(doc_content: str) -> dict[str, int]:
    try:
        raise NotImplementedError
    except NotImplementedError:
        print("Not implemented")


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


def main():
    # HashMap[filePath, HashMap[String, usize]]
    all_documents = dict[str, dict[str, int]]

    for doc in listdir("."):
        doc_content = read_doc(doc)
        if doc_content:
            lexer = Lexer(doc_content)
            for i in lexer:
                if i:
                    print("".join(i))


if __name__ == "__main__":
    main()
