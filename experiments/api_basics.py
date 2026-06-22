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


def get_post_by_id(request,post_id):
    for post in posts:
        if post['id']== post_id:
            return post
        
    return None

print(get_post_by_id("dummy_request", 1))



def create_post(request):
    title=request['title']
    id=request['id']
    posts.append({'title':title,'id':id})

create_post({'title':"mmd title",'id':4})
print(posts)