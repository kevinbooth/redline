from .car_endpoint_tests import BaseViewTest as CarBase, CarEndpointTest
from .task_endpoint_tests import BaseViewTest as TaskBase, TaskEndpointTest
from .part_endpoint_tests import BaseViewTest as PartBase, PartEndpointTest

__all__ = [
    'CarBase',
    'CarEndpointTest',
    'TaskBase',
    'TaskEndpointTest',
    'PartBase',
    'PartEndpointTest'
]
