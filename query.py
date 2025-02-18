from jinja2 import Environment, FileSystemLoader
import os

def generate(target_class, subset_properties, namespace, prefix="ns", annotation_property=None):
    current_dir = os.path.dirname(os.path.abspath(f"{__file__}/"))
    env = Environment(loader=FileSystemLoader(current_dir))
    template_obj = env.get_template(f'/templates/{subset_properties}.jinja2')

    inputs = { 'uri' : namespace,
               'prefix' : prefix,
               'class': target_class,
               'annotation_property': annotation_property }

    with open(f"queries/{subset_properties}.rq", "w") as f:
        f.write(template_obj.render(inputs))
