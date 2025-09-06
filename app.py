from domain.customer import Customer
from repository.in_memory_customer_repository import InMemoryCustomerRepository

if __name__ == "__main__":
    repo = InMemoryCustomerRepository()

    # Add customers
    repo.add(Customer(1, "Alice", "alice@example.com"))
    repo.add(Customer(2, "Bob", "bob@example.com"))

    # Retrieve one customer
    print(repo.get_by_id(1))

    # List all customers
    print(repo.list_all())
