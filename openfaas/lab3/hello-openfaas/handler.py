def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    ret_str = 'Hello OpenFaas. I received the following text:\n'
    return ret_str + req
