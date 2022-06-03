
from jinja2 import Environment, FileSystemLoader
import yaml
import os


class DagCreator:

    @staticmethod
    def create(template_file_path, config_file_path, dag_home):
        template_dir = os.path.dirname(os.path.abspath(template_file_path))
        template_file_name = os.path.basename(os.path.abspath(template_file_path))

        print(template_dir)
        print(template_file_name)

        env = Environment(loader=FileSystemLoader(template_dir))
        ref_template = env.get_template(template_file_name)

        with open(config_file_path, 'r') as config_file_ref:
            yaml_config = yaml.safe_load(config_file_ref)
            dag_file_name = f"dag_{yaml_config['dag_id']}".lower()

            with open(f"{dag_home}/{dag_file_name}.py", 'w') as dag_file_ref:
                dag_file_ref.write(ref_template.render(yaml_config))


if __name__ == '__main__':
    creator = DagCreator()
    creator.create("examples/templates/dag_bash_template.jinja2", "examples/configs/dag_bash_config.yml", "./")
