🏥 Hospital Management System (OOP Project)
📌 Overview

This project is a fully object-oriented Hospital Management System implemented in Python.
It models real-world hospital operations such as managing patients, doctors, rooms, and appointments with strong validation, indexing, and conflict prevention.

The system is designed with clean OOP principles, including abstraction, encapsulation, inheritance, and polymorphism.

✨ Features
👤 People Management
Add, remove, and search patients and doctors
Unique ID validation (4-digit IDs)
Strong type and value validation for all attributes
Equality based on unique ID
Hashable objects (usable in sets/dicts)
🏥 Room Management
Add and remove hospital rooms
Room validation (3-digit room numbers)
Department assignment per room
Room indexing for fast lookup
📅 Appointment System
Create appointments between:
Patient
Doctor
Room
Prevents scheduling conflicts:
Doctor double-booking
Patient double-booking
Room double-booking


Supports:
Appointment cancellation
Automatic unlinking from all entities

🧠 Hospital Core System
Central management of all entities
Fast lookup using dictionaries (indexing system)
Safe deletion with cascading appointment removal
System integrity protection



🧪 Advanced Python Features Used
Abstract Base Classes (ABC)
Properties with validation
Magic methods:
__repr__, __str__
__eq__, __hash__
__len__, __contains__
__iter__, __getitem__
Iterable hospital (patients iteration)
Immutable external views (tuples instead of lists)


🧱 Project Structure


Person (Abstract Base Class)
│
├── Patient
├── Doctor
│
Room
│
Appointment
│
Hospital (Main Controller)




⚙️ How It Works
1. Create Entities
Patients, doctors, and rooms are created with strict validation.
2. Register in Hospital
Entities are added to the hospital system with indexing for fast retrieval.
3. Create Appointments
Appointments connect patient + doctor + room + time
System checks:
Time conflicts
Availability of all entities
Past date restriction
4. Manage System
Remove patients/doctors/rooms safely
Automatically removes or cancels related appointments


▶️ How to Run

Make sure you have Python 3.8+ installed.

python your_file_name.py

The script includes a full stress test section that automatically:

Creates sample data
Tests edge cases
Validates system integrity
Prints results to console

🧪 Testing Included

The built-in test suite covers:

✔ Valid entity creation
✔ Duplicate prevention
✔ Invalid input handling
✔ Appointment conflict detection
✔ Past date rejection
✔ Cancellation system
✔ Deletion cascade effects
✔ Magic methods behavior
✔ Iteration & membership checks
✔ Dictionary/set integration
🧠 Design Highlights
🔹 Strong Data Integrity

Every class validates input strictly to prevent invalid state.

🔹 Fast Lookup System

Uses dictionaries (ID → object) for O(1) retrieval.

🔹 Safe Relationship Handling

Appointments are automatically synchronized across:

Patient
Doctor
Room
Hospital
🔹 Encapsulation

Internal lists are protected and exposed as immutable tuples.

🚀 Possible Improvements
Add persistent storage (database or JSON)
Add GUI (Tkinter / PyQt / Web dashboard)
Add authentication system (admin/doctor roles)
Add appointment rescheduling feature
Add logging system for actions
Add search filters (by date, doctor, department)
👨‍💻 Author Notes

This project demonstrates advanced OOP design in Python and simulates a real hospital management workflow with strong focus on correctness, validation, and system integrity.
