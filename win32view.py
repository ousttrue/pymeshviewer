import windowsapi

class MyWindow(windowsapi.OpenGLWindow):

    def onResize(self, w, h):
        pass

    def onDraw(self):
        pass


def createWindow(w, h):
    f=windowsapi.factory()
    wndclass=f.register_class("PyMeshViewer")
    window=f.create(MyWindow, "pymeshviewer", wndclass)
    window.show()
    window.setSize(w, h)
    window.createContext(16)
    return window

