from math import log10

type DocFreq = dict[str, int]
type TermFreq = dict[str, int]


class Doc:
    def __init__(self, tf: TermFreq, count: int) -> None:
        self.tf: TermFreq = tf
        self.count: int = count


type Docs = dict[str, Doc]


class Model:
    def __init__(self, docs: Docs, df: DocFreq) -> None:
        self.docs: Docs = docs
        self.df: DocFreq = df


def compute_tf(t: str, doc: Doc) -> float:
    return float(doc.tf[t]) / float(doc.count)


def compute_idf(t: str, n: int, df: DocFreq) -> float:
    return log10(float(n) / float(df[t]))
