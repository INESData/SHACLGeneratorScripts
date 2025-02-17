from jinja2 import Environment, FileSystemLoader
import yaml
import os, subprocess

def generate(target_class, subset_properties, namespace):
    current_dir = os.path.dirname(os.path.abspath(f"{__file__}/"))
    env = Environment(loader=FileSystemLoader(current_dir))
    template_obj = env.get_template(f'/templates/{subset_properties}.jinja2')

    inputs = { 'uri' : namespace,
               'class': target_class
                }

    with open(f"queries/{subset_properties}.rq", "w") as f:
        f.write(template_obj.render(inputs))
