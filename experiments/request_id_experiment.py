# Middleware Lifecycle:
# __init__  → runs once when Django loads the middleware (stores get_response pipeline)
# __call__  → runs on every single request (handles request/response cycle)
# get_response → the next step in Django pipeline (next middleware or final view)

import uuid

class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Generate request ID
        request_id = str(uuid.uuid4())

        # Attach to request object
        request.request_id = request_id

        # Process request
        response = self.get_response(request)

        # Attach to response headers
        response["X-Request-ID"] = request_id

        return response