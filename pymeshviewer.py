#!/usr/bin/env python
# coding: utf-8
"""
this script require pyOpenGL, PIL, numpy.
"""

import sys
import os
import win32con
from ctypes import *

import glglue.wgl
import opengl
import opengl.rokuro
import mqobuilder
import pmdbuilder
import pmxbuilder


class MyWindow(glglue.wgl.Window):
    def __init__(self):
        glglue.wgl.Window.__init__(self)
        self.view=opengl.rokuro.RokuroView()
        self.controller=opengl.BaseController(self.view)

    def onOpen(self):
        path=tkinter_filedialog.askopenfilename(
                filetypes=[
                    ('poloygon model files', '*.mqo;*.pmd;*.pmx'),
                    ], 
                initialdir=self.current)
        self.current=os.path.dirname(path)
        self.load(path)

    def load(self, path):
        model=self.loadModel(path)
        if not model:
            print('fail to load %s' % path)
            return
        print('load %s' % path)
        print(model)
        self.controller.setRoot(model)
        bb=model.get_boundingbox()
        print(bb)
        self.view.look_bb(*bb)

    def loadModel(self, path):
        if path.lower().endswith(".mqo"):
            return mqobuilder.build(path)
        elif path.lower().endswith(".pmd"):
            return pmdbuilder.build(path)
        elif path.lower().endswith(".pmx"):
            return pmxbuilder.build(path)
        else:
            print("unknown file format: {0}".format(path))

    def onKeyDown(self, event):
        key=event.keycode
        if key==27:
            # Escape
            sys.exit()
        if key==81:
            # q
            sys.exit()
        else:
            print("keycode: %d" % key)


if __name__ == '__main__':
    factory=glglue.wgl.WindowFactory()
    window=factory.create(MyWindow)
    window.createGLContext(16)
    if len(sys.argv)>1:
        window.load(sys.argv[1])
    window.Show()
    import sys
    sys.exit(factory.loop())

