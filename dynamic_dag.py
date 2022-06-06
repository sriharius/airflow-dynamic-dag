
import argparse

import yaml
from creator.dag_creator import DagCreator


class AbstractDynamicDagCreator:

    def __init__(self, args: dict):
        self.creator_args = args

    def create(self):
        pass


class SingleDynamicDagCreator(AbstractDynamicDagCreator):
    """ Dynamic DAG creation based one combination of template and yaml config file """
    def create(self):
        creator = DagCreator(self.creator_args['template_file'],
                    self.creator_args['config_file'],
                    self.creator_args['dag_home'])
        
        creator.create()


class MultipleDynamicDagCreator(AbstractDynamicDagCreator):
    """ Dynamic DAG creation based on a profile based mapping configuration file """
    def create(self):
        with open(self.creator_args['profile_file'], 'r') as profilefile:
            content = yaml.safe_load(profilefile)
        
            for key in content.keys():
                template_file = content[key]['template_file']
                config_file = content[key]['config_file']
                
                creator = DagCreator(template_file, config_file, self.creator_args['dag_home'])
                creator.create()


class DynamicDagFactory():

    @staticmethod
    def get_dag_creator(args: dict) -> AbstractDynamicDagCreator:
        if args['cmd'] == 'single':
            return SingleDynamicDagCreator(args)
        elif args['cmd'] == 'multiple':
            return MultipleDynamicDagCreator(args)
        else:
            raise ValueError('Unknown command')


# Command Line arguments
# Flag - Single or Multiple should be mutually exclusive
# For Single, template_file and yaml_file path should be provided
# For multiple, profile_file path should be provided
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dynamic DAG Creation')
    parser.add_argument('-d', '--dag_home', required=True, help='Absolute path to folder where DAG are created')

    sp = parser.add_subparsers(title='sub commands', description='valid commands', help='additional help')
    single_dd_parser = sp.add_parser('single')
    multiple_dd_parser = sp.add_parser('multiple')

    single_dd_parser.set_defaults(cmd='single')
    multiple_dd_parser.set_defaults(cmd='multiple')

    single_dd_parser.add_argument('-t', '--template_file', required=True, help='Absolute path to the template file')
    single_dd_parser.add_argument('-c', '--config_file', required=True, help='Absolute path to the YAML configuration file')

    multiple_dd_parser.add_argument('-p', '--profile_file', required=True, help='Absolute path to the profile file')

    cmd_args = parser.parse_args()
    creator = DynamicDagFactory.get_dag_creator(vars(cmd_args))
    creator.create()
