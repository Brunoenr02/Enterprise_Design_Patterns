from domain.customer import Customer
from repository.in_memory_customer_repository import InMemoryCustomerRepository

def test_add_and_retrieve_customer():
    repo = InMemoryCustomerRepository()
    customer = Customer(1, "Test User", "test@example.com")
    repo.add(customer)
    assert repo.get_by_id(1) == customer

def test_list_all_customers():
    repo = InMemoryCustomerRepository()
    repo.add(Customer(1, "Alice", "alice@example.com"))
    repo.add(Customer(2, "Bob", "bob@example.com"))
    customers = repo.list_all()
    assert len(customers) == 2
