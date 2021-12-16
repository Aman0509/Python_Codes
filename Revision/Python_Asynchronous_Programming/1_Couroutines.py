"""
To understand it more clearly, checkout 
- https://stackabuse.com/coroutines-in-python
- https://www.youtube.com/watch?v=T3tmkWfOHa8 
- https://www.integralist.co.uk/posts/python-generators/#why-use-coroutines
"""

def couroutine(func):
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f
    return wrapper

@couroutine
def search():
    random_text = """
    It's not only writers who can benefit from this free online tool. If you're a programmer who's working on a project where blocks of text are needed, this tool can be a great way to get that. It's a good way to test your programming and that the tool being created is working well.
    """
    while True:
        input_text = yield
        if input_text in random_text:
            print("Yes")
        else:
            print("No")
print("searhing...")
s = search()
s.send("text")
s.send("great")
s.send("road")

