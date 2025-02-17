from rdflib import Graph

def load(ontology_path):
    g = Graph()
    g.parse(ontology_path)

    print("Ontology successufully parsed! (", len(g), "triples )")

    return g


def get_namespace(g):
  for ns_prefix, namespace in g.namespaces():
    if not ns_prefix:
      return namespace
  return ""
