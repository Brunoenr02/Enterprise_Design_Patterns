# Enterprise Design Patterns

A Python implementation demonstrating key enterprise design patterns, specifically focusing on the Repository pattern and Domain-Driven Design (DDD) principles.

## 🏗️ Architecture Overview

This project showcases a clean architecture approach with clear separation of concerns:

- **Domain Layer**: Contains business entities and core domain logic
- **Repository Layer**: Provides data access abstraction
- **Application Layer**: Orchestrates domain objects and repositories

## 📁 Project Structure

```
Enterprise_Design_Patterns/
├── domain/
│   └── customer.py              # Customer domain entity
├── repository/
│   ├── customer_repository.py   # Repository interface (abstract base)
│   └── in_memory_customer_repository.py  # In-memory implementation
├── tests/
│   └── test_customer_repository.py  # Unit tests
├── app.py                       # Main application entry point
└── .github/workflows/
    └── python-ci.yml           # GitHub Actions CI/CD pipeline
```

## 🎯 Design Patterns Implemented

### 1. Repository Pattern
The Repository pattern encapsulates the logic needed to access data sources, centralizing common data access functionality.

**Benefits:**
- Decouples the infrastructure or technology used to access databases from the domain model layer
- Makes testing easier by providing a consistent interface
- Allows for easy switching between different data storage implementations

**Implementation:**
- `CustomerRepository`: Abstract base class defining the contract
- `InMemoryCustomerRepository`: Concrete implementation using in-memory storage

### 2. Domain-Driven Design (DDD)
The project follows DDD principles by organizing code around the business domain.

**Key Elements:**
- **Domain Entity**: `Customer` class represents a core business concept
- **Repository**: Provides a collection-like interface for accessing domain objects
- **Clear Boundaries**: Separation between domain logic and data access concerns

## 🚀 Features

- **Customer Management**: Create, retrieve, and list customers
- **Type Safety**: Uses Python type hints for better code quality
- **Clean Architecture**: Clear separation of concerns
- **Unit Testing**: Comprehensive test coverage
- **CI/CD Pipeline**: Automated testing with GitHub Actions

## 🛠️ Technologies Used

- **Python 3.11+**: Modern Python features and type hints
- **pytest**: Testing framework
- **GitHub Actions**: Continuous integration and deployment

## 📋 Requirements

- Python 3.11 or higher
- pytest (for running tests)

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Brunoenr02/Enterprise_Design_Patterns.git
   cd Enterprise_Design_Patterns
   ```

2. **Install dependencies:**
   ```bash
   pip install pytest
   ```

## 🏃‍♂️ Usage

### Running the Application

```bash
python app.py
```

This will demonstrate:
- Creating customers
- Adding them to the repository
- Retrieving individual customers
- Listing all customers

### Running Tests

```bash
pytest
```

Or for verbose output:
```bash
pytest -v
```

## 📖 Code Examples

### Creating and Using a Customer

```python
from domain.customer import Customer
from repository.in_memory_customer_repository import InMemoryCustomerRepository

# Create a repository
repo = InMemoryCustomerRepository()

# Create a customer
customer = Customer(1, "John Doe", "john.doe@example.com")

# Add to repository
repo.add(customer)

# Retrieve customer
retrieved_customer = repo.get_by_id(1)
print(retrieved_customer)  # Customer(id=1, name='John Doe', email='john.doe@example.com')

# List all customers
all_customers = repo.list_all()
```

### Extending with New Repository Implementations

To add a new storage backend (e.g., database), simply implement the `CustomerRepository` interface:

```python
from repository.customer_repository import CustomerRepository

class DatabaseCustomerRepository(CustomerRepository):
    def add(self, customer: Customer) -> None:
        # Database implementation
        pass
    
    def get_by_id(self, customer_id: int) -> Optional[Customer]:
        # Database implementation
        pass
    
    def list_all(self) -> List[Customer]:
        # Database implementation
        pass
```

## 🧪 Testing

The project includes comprehensive unit tests that verify:
- Adding customers to the repository
- Retrieving customers by ID
- Listing all customers
- Repository behavior with multiple customers

### Test Structure

```python
def test_add_and_retrieve_customer():
    repo = InMemoryCustomerRepository()
    customer = Customer(1, "Test User", "test@example.com")
    repo.add(customer)
    assert repo.get_by_id(1) == customer
```

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions workflow that:
- Runs on Python 3.11
- Installs dependencies automatically
- Executes all tests
- Provides feedback on code quality

## 🎓 Learning Objectives

This project demonstrates:

1. **Repository Pattern**: How to abstract data access logic
2. **Dependency Inversion**: Depending on abstractions, not concretions
3. **Single Responsibility**: Each class has a single, well-defined purpose
4. **Open/Closed Principle**: Easy to extend with new repository implementations
5. **Interface Segregation**: Clean, focused interfaces
6. **Domain-Driven Design**: Organizing code around business concepts

## 📝 License

This project is open source and available under the MIT License.

