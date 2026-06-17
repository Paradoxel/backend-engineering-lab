# Fake Django view (final destination of request)
def view(request):
    print("View executed")  # This runs when request reaches the view
    return "response"       # Simulated HTTP response


class MiddlewareA:
    def __init__(self, get_response):
        self.get_response = get_response  # Next layer in the middleware chain (view or another middleware)

    def __call__(self, request):
        print("Middleware A -> Request")  # Runs on request phase (before view)

        response = self.get_response(request)  # Pass request to next middleware/view

        print("Middleware A -> Response")  # Runs on response phase (after view returns)

        return response  # Return response back up the chain


# Build middleware chain (wrap view inside middleware)
app = MiddlewareA(view)

# Simulate HTTP request
app("request")