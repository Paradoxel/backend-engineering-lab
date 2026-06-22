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
# GET all of items
def get_posts(request):
    return posts

print(get_posts("dummy_request"))

# GET an item with key or id or slug and etc
def get_post_by_id(request,post_id):
    for post in posts:
        if post['id']== post_id:
            return post
        
    return None

print(get_post_by_id("dummy_request", 1))


# CREATE a post with needed info
def create_post(request):
    title=request['title']
    id=request['id']
    posts.append({'title':title,'id':id})

create_post({'title':"mmd title",'id':4})
print(posts)


# PUT
def update_post(request,post_id):
    for post in posts:
        if post['id']==post_id:
            post['title']=request['title']
            return post
    print("Not FOUND posts")
    return None

update_post({'title':"EDITED TITLE 1"},1)
print(posts)