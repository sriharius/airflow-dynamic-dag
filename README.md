
# Airflow Dynamic DAG

Create Airflow DAGs dynamic using YAML configuration file

# Introduction
Airflow Dynamic DAG is a framework which provides ability create DAG files using templates and configuration provided by a YAML file. This means every configuration will lead to a auto generated DAG file which can be loaded by the Airflow scheduler.

Why create individual DAG files rather than creating DAG objects at runtime? Well, Airflow scheduler scan DAG folder in an interval; if the time take to create multiple DAG objects, is more than the scan interval, the Airflow scheduler will crash. To avoid this, if the files are created ahead of time, the scheduler will load the files wherever there is import of airflow.DAG mentioned. This approach is much more scalable when there are many DAGs.

# Key Features
- Create static DAG file with a template and YAML configuration file
- Create multiple DAG files by creating profile configuration file
- Manage multiple profiles for different environments


# Usage
Clone the project, to invoke the commands for creating the DAGs

On clone, go to root directory `airflow-dynamic-dag`.

Run `python dynamic_dag.py --help` This will print the usage as shown below

```
usage: dynamic_dag.py [-h] -d DAG_HOME {single,multiple} ...

Dynamic DAG Creation

optional arguments:
  -h, --help            show this help message and exit
  -d DAG_HOME, --dag_home DAG_HOME
                        Absolute path to folder where DAG are created

sub commands:
  valid commands

  {single,multiple}     additional help
```

**To create a single DAG file**

Run the command 

`python dynamic_dag.py single -t '/path/to/template/file.jinja2' -c /path/to/config.yaml' -d '/path/to/dag/home'`

**To create multiple DAG files using profile configuration file**

Run the command 

`python dynamic_dag.py multiple -d '/path/to/dag/home' -p /path/to/profile.yaml`

Checkout the `airflow-dynamic-dag/examples` folder for the sample templates and configuration files

If the code runs successfully, there will be a dag file created at the `dag_home` folder.

# Features or Bugs
Please raise a issue with the required information.
