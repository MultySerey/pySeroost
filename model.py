from math import log10

DocFreq = dict[str, int]
TermFreq = dict[str, int]


class Doc:
    def __init__(self, tf: TermFreq, count: int) -> None:
        self.tf: TermFreq = tf
        self.count: int = count


Docs = dict[str, Doc]


class Model:
    def __init__(self, docs: Docs, df: DocFreq) -> None:
        self.docs: Docs = docs
        self.df: DocFreq = df


def compute_tf(t: str, doc: Doc) -> float:
    n: float = float(doc.count)
    m: float = float(doc.tf[t])
    return m / n


def compute_idf(t: str, n: int, df: DocFreq) -> float:
    m: float = float(df[t])
    return log10(float(n) / m)
