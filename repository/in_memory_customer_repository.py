from typing import List, Optional
from domain.customer import Customer
from repository.customer_repository import CustomerRepository

class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self):
        self._customers = {}

    def add(self, customer: Customer) -> None:
        self._customers[customer.customer_id] = customer

    def get_by_id(self, customer_id: int) -> Optional[Customer]:
        return self._customers.get(customer_id)

    def list_all(self) -> List[Customer]:
        return list(self._customers.values())
