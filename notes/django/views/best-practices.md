# Views Best Practices

## Keep Views Thin

A View should coordinate the request, not contain all the business logic.

❌ Bad

- Long calculations
- Complex validation
- Business rules

✅ Good

- Call services
- Call models
- Return a response

---

## Choose the Right View

- FBV → Simple views
- CBV → Reusable views
- Generic CBV → Standard CRUD operations

---

## Follow DRY

Avoid duplicating the same logic.

Prefer:

- Generic Views
- Mixins
- Helper functions

---

## Return the Correct Response

Views should always return an `HttpResponse`.

Examples:

- HttpResponse
- JsonResponse
- Redirect
- render()

---

## Prefer Readability

Readable code is better than clever code.

---

## Summary

- Keep Views small.
- Move business logic elsewhere.
- Reuse code with Mixins.
- Use Generic Views when appropriate.
- Write readable code.