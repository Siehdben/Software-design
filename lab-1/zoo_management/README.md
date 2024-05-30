# Zoo Management System

## Principles Demonstrated

### 1. DRY (Don't Repeat Yourself)
- Each class and method is designed to be reusable and avoids redundancy.
- For example, the `Animal` class is used both in `Enclosure` and `Inventory` classes.

### 2. KISS (Keep It Simple, Stupid)
- The design of the classes is straightforward and easy to understand.
- Methods are concise and serve a single purpose.

### 3. SOLID Principles
#### a. Single Responsibility Principle (SRP)
- Each class has a single responsibility. For example, the `Animal` class only deals with animal attributes.
#### b. Open/Closed Principle (OCP)
- Classes are open for extension but closed for modification. We can extend functionality by creating new classes without changing existing ones.
#### c. Liskov Substitution Principle (LSP)
- Objects of a superclass should be replaceable with objects of a subclass without affecting the functionality. Our system adheres to this as we use base class instances (like `Animal`) where needed.
#### d. Interface Segregation Principle (ISP)
- Our design avoids forcing any class to implement methods they do not use. For example, `Animal` and `Enclosure` have distinct interfaces.
#### e. Dependency Inversion Principle (DIP)
- High-level modules are not dependent on low-level modules. Both depend on abstractions. Our design does not strictly enforce this principle, but it is not violated either.

### 4. YAGNI (You Aren't Gonna Need It)
- The system is built with only the necessary features to meet the requirements, avoiding over-engineering.

### 5. Composition Over Inheritance
- The `Enclosure` class contains `Animal` objects via composition, demonstrating the preference for composition.

### 6. Program to Interfaces, Not Implementations
- Our system defines classes with clear interfaces and uses these interfaces to interact with objects, rather than concrete implementations.

### 7. Fail Fast
- The design encourages immediate feedback if incorrect data is provided, e.g., adding only `Animal` objects to an `Enclosure`.

## Files
- [animal.py](animal.py): Defines the `Animal` class.
- [enclosure.py](enclosure.py): Defines the `Enclosure` class.
- [food.py](food.py): Defines the `Food` class.
- [zooworker.py](zooworker.py): Defines the `ZooWorker` class.
- [inventory.py](inventory.py): Defines the `Inventory` class.
- [main.py](main.py): Contains the main method to run the system.
