# %%
from rdflib import Graph
import ontology

def construct(knowledge_graph, shapes_path, subset_properties):
    g = knowledge_graph
    with open("queries/"+subset_properties+".rq", encoding="utf-8") as f:
        read_query = f.read()

    qres = g.query(read_query)
    print(f"SHACL shapes successufully constructed! \n({len(qres)} triples)")

    qres.serialize(destination=shapes_path, format="ttl")

