import os
from datetime import datetime

from airflow.models import DAG
from airflow.models import TaskInstance

from solution5 import FindCommonOperator


def test_execute(tmpdir):
    # setup for doing the test
    with open(os.path.join(tmpdir.strpath, "1983.txt"), 'w') as first_file:
        first_file.write("ian,M,2")
    with open(os.path.join(tmpdir.strpath, "1993.txt"), 'w') as second_file:
        second_file.write("Austin,M,1")

    dag = DAG(dag_id='test_dag', start_date=datetime.now())
    task = FindCommonOperator(dag=dag, task_id='test_task', names_directory=tmpdir.strpath)
    ti = TaskInstance(task=task, execution_date=datetime.now())

    result = task.execute(ti.get_template_context())
    assert result == "ian"
