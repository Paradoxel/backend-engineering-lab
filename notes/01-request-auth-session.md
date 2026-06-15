#Request ID

🧩 Definition
A Request ID is a unique identifier assigned to each HTTP request to trace it through the full Django request–response cycle.

🎯 Purpose

1. Debugging production issues
2. Tracking logs for a single request
3. Connecting logs across services
4. Monitoring performance issues

⚙️ How it is generated
Django does not include request_id in logs by default.
It is usually implemented using middleware.

import uuid

request_id = str(uuid.uuid4())

🧠 Why it is unique

1. UUID is 128-bit
2. Collision chance is extremely low
3. Safe for distributed systems

🔄 Django Request Lifecycle with Request ID

1. Request enters Django
2. Middleware stack starts
3. Request ID is generated
4. It is attached to request + logs
5. AuthenticationMiddleware sets request.user
6. View executes
7. Response returned
8. Middleware finishes


#User ID

🧩 Definition

A User ID is a unique identifier that represents the authenticated user in Django.
It is used to identify who is making the request and is reconstructed on every request using session data.

🎯 Purpose
1. Identify the authenticated user
2. Personalize application behavior per user
3. Track user actions in logs
4. Enforce permissions and access control
5. Support auditing and security monitoring

⚙️ How it works

Django does not store user_id inside the request permanently.
Instead, it is rebuilt on every request using the session system.

Flow:
1. User logs in
2. Django stores _auth_user_id in session (server-side)
3. Browser stores only sessionid cookie
4. On every request:
5. Django reads sessionid
6. Loads session data from server
7. Reconstructs request.user
8. request.user.id becomes available

🧠 Why it is stable
User ID is stored in the database (primary key)
Session only references the user ID
Request object is rebuilt every time, not stored
Identity remains consistent across requests

🔄 Django Authentication Lifecycle with User ID
1. User logs in
2. Session is created on server
3. _auth_user_id is stored in session
4. Browser receives sessionid cookie
5. New request arrives with cookie
6. SessionMiddleware loads session data
7. AuthenticationMiddleware reconstructs request.user
8. request.user.id is available
9. View executes
10. Response is returned

⚡ Key Insight
User ID is persistent (database-level)
Session stores only a reference to the user
request.user is recreated on every request
Nothing is permanently stored in the request object