def login(username, password):
    # simple login check
    if username and password:
        print("Login successful")
        return True
    return False