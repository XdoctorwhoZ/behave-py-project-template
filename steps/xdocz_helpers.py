import base64

COLOR_LOG='\033[93m'
COLOR_END='\033[0m'

###############################################################################
###############################################################################

def AttachTextLog(context, log):
    """ 
    """
    print(COLOR_LOG, log, COLOR_END,"\n")
    context.attach("text/plain", log)

###############################################################################
###############################################################################

def ImgToBase64String(img_filepath):
    """ To import an image file and convert it into base64 string to context.attach
    """
    return base64.b64encode(open(img_filepath, "rb").read()).decode('ascii')

###############################################################################
###############################################################################

