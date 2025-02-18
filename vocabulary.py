from rdflib import Graph
import ontology

def join(ontology_path, vocabulary_path=None):
  g = ontology.load(ontology_path)
  print("Ontology successufully parsed!")

  if vocabulary_path:
    g.parse(vocabulary_path)
    print("Skos concepts successufully parsed!")
  print(f"({len(g)} triples)")
  return g