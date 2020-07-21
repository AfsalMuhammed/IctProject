import eel
import utils.snipping_tool as snipping_tool
import utils.file_opener as FileOpener


# Set web files folder
eel.init("web")


@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print("Hello from %s" % x)
    snipping_tool.image_grab()
    return "a string"


@eel.expose
def fileHandling(x):
    print("Hello from %s" % x)
    a = FileOpener.image_open()
    print(a)
    return "File Copied to Directory"


eel.start("hello.html", size=(300, 200))

