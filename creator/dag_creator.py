
from jinja2 import Environment, FileSystemLoader
import yaml
import os

from creator.validate_variables import VariableValidator


class DagCreator:
    """ Class to crate the static DAG file based on the template and YAML configuration file
        template_file: str
            absolute path to the template file
        config_file: str
            absolute path to the YAML configuration file
        dag_home: str
            absolute path to the directory where the DAG file should be created
    """
    def __init__(self, template_file, config_file, dag_home):
        self.template_file_path = template_file
        self.config_file_path = config_file
        self.dag_home = dag_home

    def create(self):
        # check the variables in template file and YAML config keys for a match
        validator = VariableValidator(self.template_file_path, self.config_file_path)
        if not validator.validate():
            print("Template variables are not matching with YAML configuration")
            print(f"DAG file generation for {self.template_file_path} and {self.config_file_path} failed")
            return

        template_dir = os.path.dirname(os.path.abspath(self.template_file_path))
        template_file_name = os.path.basename(os.path.abspath(self.template_file_path))

        env = Environment(loader=FileSystemLoader(template_dir))
        ref_template = env.get_template(template_file_name)

        with open(self.config_file_path, 'r') as config_file_ref:
            yaml_config = yaml.safe_load(config_file_ref)
            dag_file_path = os.path.join(self.dag_home, f"dag_{yaml_config['dag_id']}.py".lower())

            print(f'Generating DAG file for {self.template_file_path} and {self.config_file_path} at {self.dag_home}')

            with open(dag_file_path, 'w') as dag_file_ref:
                dag_file_ref.write(ref_template.render(yaml_config))
                print(f'DAG file {dag_file_path} is generated successfully')
