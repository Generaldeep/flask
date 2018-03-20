    users = [
        {
            'id': 1,
            'username': 'deep',
            'password': 'whatitdo'
        }
    ]

username_mapping = {
    'deep': {
        'id': 1,
        'username': 'deep',
        'password': 'whatitdo'
    }
}

userid_mapping = {
    1: {
        'id': 1,
        'username': 'deep',
        'password': 'whatitdo'
    }
}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user
