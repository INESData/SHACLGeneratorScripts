# %%
import os
import argparse
import ontology, shapes, query, vocabulary
# %%
parser = argparse.ArgumentParser(
    prog='construct_shacl',
    description='Construct SHACL shapes from OWL files.',
    )

parser.add_argument('ontology', metavar='ontology', help='path to OWL ontology input file')
parser.add_argument('shapes', metavar='shapes', help='path to SHACL shapes output file')
parser.add_argument('target', metavar='target', help='target class name (without any prefix or namespace)')
parser.add_argument('subset_properties', metavar='subset_properties', help="target subset properties ('datatype_properties' or 'object_properties')")
parser.add_argument('-v', '--vocabulary', metavar='vocabulary', help="path to SKOS vocabulary input file and the inScheme ontology annotation property used (with prefix)", nargs=2)
parser.add_argument('-p', '--prefix', metavar='prefix', help=" preferred namespace prefix", default='ns')

args = parser.parse_args()

ontology_path = args.ontology
shapes_path = args.shapes
target_class = args.target
subset_properties = args.subset_properties
vocabulary_path = args.vocabulary[0]
annotation_property = args.vocabulary[1]
prefix = args.prefix

ns = ontology.get_namespace(ontology_path)
kg = vocabulary.join(ontology_path, vocabulary_path)
query.generate(target_class, subset_properties, ns, prefix, annotation_property)
shapes.construct(kg, shapes_path, subset_properties)