# SHACL Generator Scripts
Command line SHACL shapes generator from OWL ontologies. It is based on the RDFlib library, which supports multiple serializations of OWL ontologies and SPARQL queries.

## To run the application:
1. Make sure you have Python 3 installed.
2. Clone the current repository.
3. Navigate to the folder containing the `requirements.txt` file.
4. Run `pip install -r requirements.txt`.
5. Now you should be able to run the `construct_shacl.py` command line app as described below.

_The application provided was developed using Python version 3.10.12_

## Usage

    usage: construct_shacl.py [-h] ontology shapes target subset_properties

    Construct SHACL shapes from OWL files.

    positional arguments:
    *  ontology           path to OWL ontology input file
    *  shapes             path to SHACL shapes output file
    *  target             target class name (without any prefix or namespace)
    *  subset_properties  target subset properties ('datatype_properties' or 'object_properties')

The fields marked with an \* are mandatory.

### Example
```bash
python construct_shacl.py path/to/ontology.ttl path/to/shapes.ttl TargetClassName datatype_properties
```

## Options
    -h, --help     show this help message and exit


