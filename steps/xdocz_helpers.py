import base64



def ImgToBase64String(img_filepath):
    """ To import an image file and convert it into base64 string to context.attach
    """
    return base64.b64encode(open(img_filepath, "rb").read()).decode('ascii')


