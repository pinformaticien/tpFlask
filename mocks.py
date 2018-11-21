from flask import abort

class Post:


    POSTS = [
    {'id':1, 'title':'First Post', 'content':'This my first post'},
    {'id':2, 'title':'Second Post', 'content':'This my second post'},
    {'id':3, 'title':'Third Post', 'content':'This my third post'},
    ]


    @classmethod
    def all(cls):
        """fetch all posts"""
        return cls.POSTS


    @classmethod
    def find(cls, id):
        """fetch a single post"""
        try:
            return cls.POSTS[int(id)-1]
        except IndexError:
            abort(404)
