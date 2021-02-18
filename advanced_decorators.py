## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("bradley")
# new_user.is_logged_in = True
create_blog_post(new_user)


# ------------------------------------------------------------------------------- #

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        function(args[0], args[1])

    return wrapper


@logging_decorator
def multiply(n1, n2):
    return n1 * n2


multiply(2, 2)
