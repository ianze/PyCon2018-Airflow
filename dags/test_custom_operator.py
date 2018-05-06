from datetime import datetime
from unittest import TestCase

from airflow.models import DAG, TaskInstance
from custom_operator import PyconOperator

class TestPyconOperator(TestCase):
    def test_execute(self):
        dag = DAG(dag_id='pytn_dag',
                  start_date=datetime.now())
        task = PyconOperator(dag=dag, params={},
                             task_id='first_task')
        ti = TaskInstance(task=task,
                          execution_date=datetime.now())
        result = task.execute(ti.get_template_context())
        self.assertEqual(result, "Pycon2018")
