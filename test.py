import eel
import utils.snipping_tool as snipping_tool


# Set web files folder
eel.init("web")


@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print("Hello from %s" % x)
    snipping_tool.image_grab()
    return "a string"


# say_hello_py("Python World!")
# eel.say_hello_js("Python World!")  # Call a Javascript function

eel.start("hello.html", size=(300, 200))

