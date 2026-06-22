posts = [
    {
        "id": 1,
        "title": "First Post"
    },
    {
        "id": 2,
        "title": "Learning APIs"
    }
]

def get_posts(request):
    return posts

print(get_posts("dummy_request"))