from os import path, listdir
import docx
import pymupdf
from typing import Dict


def index_document(doc_content: str) -> Dict[str, int]:
    raise NotImplementedError


def read_doc(doc_name: str) -> str | None:
    try:
        with open(doc_name, 'rb') as f:
            match path.splitext(doc_name)[-1]:
                case ".docx":
                    return "\n".join([i.text for i in docx.Document(f).paragraphs])
                case '.pdf':
                    return "".join([page.get_text() for page in pymupdf.Document(f)])
                case _:
                    return None
    except PermissionError as e:
        print(e)
        return None


def main():
    for f in listdir("."):
        print(read_doc(f))


if __name__ == "__main__":
    main()
