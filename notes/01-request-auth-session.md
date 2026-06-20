# Request ID

## 🧩 Definition

A **Request ID** is a unique identifier assigned to each HTTP request to trace it throughout the entire Django request–response lifecycle.

---

## 🎯 Purpose

1. Debug production issues
2. Track logs for a single request
3. Correlate logs across services
4. Monitor performance and request flow

---

## ⚙️ How It Is Generated

Django does not provide a `request_id` by default.

It is commonly implemented using middleware and generated with a UUID:

```python
import uuid

request_id = str(uuid.uuid4())
```

---

## 🧠 Why It Is Unique

1. UUID uses a 128-bit value
2. Collision probability is extremely low
3. Suitable for distributed systems

---

## 🔄 Django Request Lifecycle with Request ID

1. Request enters Django
2. Middleware stack starts
3. Request ID is generated
4. Request ID is attached to the request object
5. AuthenticationMiddleware sets `request.user`
6. View executes
7. Response is generated
8. Middleware processing finishes

---

## ⚡ Key Insight

A Request ID identifies **a single HTTP request**, regardless of which user made it.

---

# User ID

## 🧩 Definition

A **User ID** is a unique identifier that represents an authenticated user in Django.

It identifies **who is making the request** and is reconstructed on every request using session data.

---

## 🎯 Purpose

1. Identify the authenticated user
2. Personalize application behavior
3. Track user actions in logs
4. Enforce permissions and access control
5. Support auditing and security monitoring

---

## ⚙️ How It Works

Django does not permanently store `user_id` inside the request object.

Instead, it reconstructs the user on every request using the session system.

### Authentication Flow

1. User logs in
2. Django stores `_auth_user_id` inside the session (server-side)
3. Browser stores only the `sessionid` cookie
4. Browser sends `sessionid` with each request
5. Django loads session data
6. AuthenticationMiddleware reconstructs `request.user`
7. `request.user.id` becomes available

---

## 🧠 Why It Is Stable

1. User ID is stored in the database
2. Sessions only reference the User ID
3. Request objects are recreated on every request
4. User identity remains consistent across requests

---

## 🔄 Django Authentication Lifecycle

1. User logs in
2. Session is created
3. `_auth_user_id` is stored in the session
4. Browser receives the `sessionid` cookie
5. Request arrives
6. SessionMiddleware loads session data
7. AuthenticationMiddleware reconstructs `request.user`
8. `request.user.id` becomes available
9. View executes
10. Response is returned

---

## ⚡ Key Insight

* User ID is persistent (database-level)
* Session stores only a reference to the user
* `request.user` is recreated on every request
* Nothing is permanently stored in the request object

---

# Logging

## 🧩 Definition

**Logging** is the process of recording application events, runtime information, warnings, and errors to provide visibility into system behavior.

---

## 🎯 Purpose

1. Debug application issues
2. Monitor system behavior
3. Track user activity
4. Record exceptions and failures
5. Trace requests across services
6. Support auditing and observability

---

## 🧠 Log Levels

| Level    | Description                                   |
| -------- | --------------------------------------------- |
| DEBUG    | Detailed diagnostic information               |
| INFO     | Normal application events                     |
| WARNING  | Unexpected but non-fatal situations           |
| ERROR    | Failed operations                             |
| CRITICAL | Severe failures requiring immediate attention |

---

## 🧠 Why Logging Matters

### Without Logging

```text
User reports a bug
        ↓
No visibility into application behavior
        ↓
Difficult investigation
```

### With Logging

```text
User reports a bug
        ↓
Check logs
        ↓
Locate request
        ↓
Identify root cause
```

---

## 🧠 Request ID and Logging

Request IDs allow developers to group all log entries belonging to a single HTTP request.

Example:

```text
[req=8f3a12] Request received
[req=8f3a12] Database query executed
[req=8f3a12] Response returned
```

---

## 🧠 User ID and Logging

User IDs help identify **who performed an action**.

Example:

```text
[user=42] Login successful
[user=42] Updated profile
[user=42] Created order
```

---

## 🔄 Typical Request Flow

```text
Request arrives
      ↓
Request ID generated
      ↓
User authenticated
      ↓
Logs written
      ↓
View executes
      ↓
Response returned
```

---

## 📄 Example Production Log

```text
2026-06-15 10:15:30 INFO request_id=abc123 user_id=42 Order created
```

---

## ⚡ One-Line Definition

Logging is the practice of recording application events and runtime information to support debugging, monitoring, auditing, and observability.


# Middleware Execution Order

## 🧠 Key Concept

- Middleware executes from **top to bottom** during the request phase
- Middleware executes from **bottom to top** during the response phase

## 🔄 Mental Model

Request:  Top → Bottom → View  
Response: Bottom → Top → Client

---

## 🔄 Middleware Execution Model

- Request phase: **FIFO (pipeline behavior)**
- Response phase: **LIFO (stack behavior)**

## 🧠 Key Insight

- Request flows through middleware in a linear pipeline (FIFO)
- Response unwinds through middleware in reverse order (LIFO)



# Session

## 🧩 Definition

A **Session** is a server-side mechanism that allows a stateless HTTP system to “remember” a user across multiple requests.

Without sessions:

\[
P(request_{n+1} | request_n) = P(request_{n+1})
\]

Each request is independent → the server forgets everything.

With sessions:

\[
P(request_{n+1} | session) \neq P(request_{n+1})
\]

Now requests become connected through a shared state.

---

## 🎯 Purpose

1. Keep user logged in  
2. Store temporary user state  
3. Connect multiple requests to one user  
4. Enable secure authentication  

---

## ⚙️ How It Works

Session works like a **key-value system**:

\[
session\_id \rightarrow user\_data
\]

- Browser stores only the key  
- Server stores the actual data  

---

## 🔐 Flow

1. User logs in  
2. Server creates a random `session_id`  
3. Server stores:

\[
session\_id \rightarrow user\_id
\]

4. Browser stores `sessionid` in cookie  
5. Every request sends this cookie  
6. Server looks up session and rebuilds user  

---

## 🍪 Storage Model

### Client
- `sessionid`

### Server
- `{ sessionid → user_id }`

---

## 🧠 Probability View (Intuition)

Without session:

\[
P(user\ identity \ on\ request_{n+1}) = 0
\]

Server has no memory → cannot identify user.

With session:

\[
P(user\ identity \ on\ request_{n+1}) = 1
\]

IF session_id is valid.

So session acts like a **perfect memory link** between requests.

---

## 🔐 Security Idea

If someone steals the session:

\[
attacker = user
\]

So security depends on:

- randomness of session_id  
- HTTPS protection  
- cookie security flags  

---

## ⚡ Key Insight

- Session ID = reference (key)  
- Server = memory (truth)  
- Browser = storage for key only  
- Session connects independent HTTP requests into one probability chain

## ⚡ One-Line Definition

A Session is a server-side state system that maps a browser-stored session ID to user identity and data, enabling persistence across stateless HTTP requests.


# JWT (JSON Web Token)

## 🧩 Definition

A **JWT (JSON Web Token)** is a cryptographically signed token that allows a client to prove its identity without requiring the server to store session data.

Unlike sessions, JWT authentication is stateless.

---

## 🎯 Purpose

1. Authenticate users without server-side session storage
2. Support distributed systems and microservices
3. Reduce dependency on centralized storage
4. Enable scalable API authentication

---

## ⚙️ Structure

A JWT consists of three parts:

```text
Header.Payload.Signature
```

### Header

Contains metadata about the token.

Example:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### Payload

Contains claims and user information.

Example:

```json
{
  "user_id": 42,
  "role": "admin"
}
```

### Signature

Used to verify that the token has not been modified.

---

## 🔄 Authentication Flow

1. User logs in
2. Server validates credentials
3. Server generates a JWT
4. JWT is returned to the client
5. Client stores the token
6. Client sends the token with each request
7. Server verifies the signature
8. User identity becomes available

---

## 🧠 Trust Model

### Session

```text
Server remembers the user
```

Identity comes from server-side memory.

### JWT

```text
Client proves identity
```

Identity comes from a valid cryptographic signature.

---

## 📊 Session vs JWT

| Feature | Session | JWT |
|----------|----------|----------|
| Storage | Server | Client |
| State | Stateful | Stateless |
| Scalability | Medium | High |
| Logout Control | Easy | Harder |
| Authentication Source | Server Memory | Token Signature |

---

## 🧠 Probability View

Session:

```text
P(user identity | valid session) = 1
```

JWT:

```text
P(user identity | valid signature, not expired) = 1
```

Both models provide deterministic identity verification, but they establish trust differently.

---

## ⚡ Key Insight

Session means:

```text
Server remembers you
```

JWT means:

```text
You prove who you are
```

---

## ⚡ One-Line Definition

JWT is a stateless authentication mechanism where user identity is carried inside a cryptographically signed token and verified on every request.




# Access Token vs Refresh Token

## 🧩 Definition

Modern authentication systems commonly use two JWT-based tokens:

1. **Access Token** → Used to access protected resources.
2. **Refresh Token** → Used to obtain new Access Tokens.

---

## 🎯 Purpose

- Limit the impact of stolen tokens.
- Reduce the frequency of user logins.
- Improve authentication security.
- Support long-lived user sessions.

---

## 🔑 Access Token

### Characteristics

- Short lifetime
- Sent with most API requests
- Contains user claims
- Expires quickly

### Typical Lifetime

- 5 minutes
- 15 minutes
- 30 minutes
- 1 hour

---

## 🔄 Refresh Token

### Characteristics

- Long lifetime
- Used infrequently
- Stored more carefully
- Not sent with every request

### Typical Lifetime

- 7 days
- 30 days
- 90 days

---

## 🧠 Key Insight

Authentication systems separate:

- **Short-Term Identity** (Access Token)
- **Long-Term Session Continuity** (Refresh Token)

This provides both security and usability.

---

## ⚡ One-Line Definition

Access Tokens provide short-lived authentication for API requests, while Refresh Tokens allow clients to securely obtain new Access Tokens without requiring the user to log in again.