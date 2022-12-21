from abc import ABC, abstractmethod

class DebitCardPaymentRepository(ABC):

    def __init__(self, db_details: str):
        self.db_details = db_details
    
    def save(self, data : dict) -> bool:
        print(self.db_details)
        print(f'DebitCardPaymentRepository data has been saved {data}')
        return True
       
