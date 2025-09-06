from abc import ABC, abstractmethod
from typing import List, Optional
from domain.customer import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def add(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self, customer_id: int) -> Optional[Customer]:
        pass

    @abstractmethod
    def list_all(self) -> List[Customer]:
        pass
