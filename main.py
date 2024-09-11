import docx
import pymupdf
from os import path, listdir


def handle_docx(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        return "\n".join([i.text for i in docx.Document(f).paragraphs])


def handle_pdf(file_path: str) -> str:
    return "".join([page.get_text() for page in pymupdf.Document(file_path)])


def handle_file(doc_name: str) -> None:
    match path.splitext(doc_name)[-1]:
        case ".docx":
            pass
            print(handle_docx(doc_name))
        case '.pdf':
            print(handle_pdf(doc_name))
        case _:
            pass


def main():
    for f in listdir("."):
        handle_file(f)


if __name__ == "__main__":
    main()
