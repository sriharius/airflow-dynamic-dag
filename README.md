
# Airflow Dynamic DAG

Create Airflow DAGs dynamic using YAML configuration file

# Introduction
Airflow Dynamic DAG is a framework which provides ability create DAG files using templates and configuration provided by a YAML file. This means every configuration will lead to a auto generated DAG file which can be loaded by the Airflow scheduler.

Why create individual DAG files rather than creating DAG objects at runtime? Well, Airflow scheduler scan DAG folder in an interval; if the time take to create multiple DAG objects, is more than the scan interval, the Airflow scheduler will crash. To avoid this, if the files are created ahead of time, the scheduler will load the files wherever there is import of airflow.DAG mentioned. This approach is much more scalable when there are many DAGs.

# Key Features
Coming Soon...

# Want To Contribute?
Please send an email to udugani@gmail.com
