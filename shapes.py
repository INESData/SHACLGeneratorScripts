# %%
from rdflib import Graph
import ontology

def construct(ontology, shapes_path, subset_properties):
    g = ontology
    with open("queries/"+subset_properties+".rq", encoding="utf-8") as f:
        read_query = f.read()

    qres = g.query(read_query)
    print("SHACL shapes successufully constructed! (", len(qres), "triples )")

    qres.serialize(destination=shapes_path, format="ttl")

