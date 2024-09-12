from math import log10

DocFreq = dict[str, int]
TermFreq = dict[str, int]


class Doc:
    tf: TermFreq
    count: int


Docs = dict[str, Doc]


class Model:
    docs: Docs
    df: DocFreq


def compute_tf(t: str, doc: Doc) -> float:
    n: float = float(doc.count)
    m: float = float(doc.tf[t])
    return m / n


def compute_idf(t: str, n: int, df: DocFreq) -> float:
    m: float = float(df[t])
    return log10(float(n) / m)
