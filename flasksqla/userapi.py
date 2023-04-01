import flasksqla.userservice  as usersrvc


def post_user(username: str):
    usersrvc.create_user(username=username)
