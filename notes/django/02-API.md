# 🌐 API Fundamentals

---

## ⚡ One-Line Definition

An API (Application Programming Interface) is a structured communication contract that defines how systems interact with each other by exchanging requests and responses in a standardized format.

It acts as an abstraction layer that hides internal implementation details while exposing only the necessary functionalities.

---

## 🧠 Why APIs Exist

Modern software systems are built in a distributed way. Different components must communicate without knowing each other's internal logic.

APIs solve this problem by providing:

- A **standard communication protocol**
- A **clear contract between systems**
- A **decoupled architecture**

This allows systems to evolve independently without breaking each other.

---

## 🔄 Request / Response Lifecycle

Every API interaction follows a predictable lifecycle:

```text id="api_flow_1"
Client
   ↓
Request
   ↓
API Layer (Routing + Validation)
   ↓
Business Logic Layer
   ↓
Data Layer (Database / Storage)
   ↓
Response
   ↓
Client