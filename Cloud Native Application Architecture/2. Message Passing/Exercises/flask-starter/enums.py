from enum import Enum

class Status(Enum):
    Queued = 'Queued'
    Processing = 'Processing'
    Completed = 'Completed'
    Failed = 'Failed'

class OrderType(Enum):
    Computer = 'Computer'