'''
In this exercise, you'll learn how to add a DAG to Airflow. To the right, you have a terminal at your disposal. The workspace comes with Airflow pre-configured, but it's easy to install on your own.

You'll need to move the dag.py file containing the DAG you defined in the previous exercise to, the DAGs folder. Here are the steps to find it:

The airflow home directory is defined in the AIRFLOW_HOME environment variable. Type echo $AIRFLOW_HOME to find out.
In this directory, find the airflow.cfg file. Use head to read the file, and find the value of the dags_folder.
Now you can find the folder and move the dag.py file there: mv ./dag.py <dags_folder>.

Which files does the DAGs folder have after you moved the file?

'''


repl:~$ echo $AIRFLOW_HOME
~/airflow
repl:~$ cd airflow/
repl:~/airflow$ head airflow.cfg
[core]
# The home folder for airflow, default is ~/airflow
airflow_home = /home/repl/airflow

# The folder where your airflow pipelines live, most likely a
# subfolder in a code repository
# This path must be absolute
dags_folder = /home/repl/airflow/dags

# The folder where airflow should store its log files
repl:~/airflow$ cd dags/
repl:~/airflow/dags$ mv ./dag.py /home/repl/airflow/dags/
mv: './dag.py' and '/home/repl/airflow/dags/dag.py' are the same file


# It has two DAG files: dag.py and dag_recommendations.py.
