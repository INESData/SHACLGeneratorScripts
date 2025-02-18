from rdflib import Graph

def load(ontology_path):
    g = Graph()
    g.parse(ontology_path)
    return g

def get_namespace(ontology_path):
  g = load(ontology_path)
  for ns_prefix, namespace in g.namespaces():
    if not ns_prefix:
      return namespace
  return ""
