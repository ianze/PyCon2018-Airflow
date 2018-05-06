from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class PyconOperator(BaseOperator):
    @apply_defaults
    def __init__(self, params,
            *args, **kwargs):
        self.params = params
        super(PyconOperator, self).__init__(
            *args, **kwargs)
    def execute(self, context):
        return "Pycon2018"
