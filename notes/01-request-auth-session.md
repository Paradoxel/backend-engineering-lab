Request ID

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