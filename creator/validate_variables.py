
from jinja2 import Environment, FileSystemLoader, nodes
import os
import yaml


class VariableValidator:
    """ Validating configuration parameters between the YAML and the template files. 
        template_path: str
            absolute path to the template file
        config_path: str
            absolution path to the YAML configuration file
    """
    def __init__(self, template_path, config_path):
        self.template_file = template_path
        self.config_file = config_path

    def _get_template_variables(self):
        # TODO nested variables are to be supported

        template_variables = set()  # used set to make sure the variables are unique

        template_dir = os.path.dirname(os.path.abspath(self.template_file))
        template_file_name = os.path.basename(os.path.abspath(self.template_file))
        env = Environment(loader=FileSystemLoader(template_dir))

        template_source = env.loader.get_source(env, template_file_name)[0]
        parsed_content = env.parse(template_source)

        if parsed_content.body and hasattr(parsed_content.body[0], 'nodes'):
            for variable in parsed_content.body[0].nodes:
                if type(variable) is nodes.Name or type(variable) is nodes.Getattr:
                    template_variables.add(variable.name)

        return template_variables

    def _get_config_keys(self):
        with open(self.config_file, 'r') as config_file_ref:
            yaml_config = yaml.safe_load(config_file_ref)
            return set(yaml_config.keys())

    def validate(self):
        template_variables = self._get_template_variables()
        config_keys = self._get_config_keys()

        return (template_variables == config_keys)
