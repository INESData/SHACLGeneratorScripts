# %%
import os
import argparse
import ontology, shapes, query
# %%
parser = argparse.ArgumentParser(
    description='Construct SHACL shapes from OWL files.'
    )

parser.add_argument('ontology', metavar='ontology', help='path to OWL ontology input file')
parser.add_argument('shapes', metavar='shapes', help='path to SHACL shapes output file')
parser.add_argument('target', metavar='target', help='target class name (without any prefix or namespace)')
parser.add_argument('subset_properties', metavar='subset_properties', help="target subset properties ('datatype_properties' or 'object_properties')")


args = parser.parse_args()

ontology_path = args.ontology
shapes_path = args.shapes
target_class = args.target
subset_properties = args.subset_properties


ont = ontology.load(ontology_path)
namespace = ontology.get_namespace(ont)
query.generate(target_class, subset_properties, namespace)
shapes.construct(ont, shapes_path, subset_properties)