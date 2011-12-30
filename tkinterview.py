#!/usr/bin/env python
# coding: utf-8
"""
this script require pyOpenGL, PIL, numpy and Togl(tck/tk).

Togl install on Windows
=======================

* download Togl2.0-8.4-Windows.zip
* copy Togl2.0-8.4-Windows/lib/Togl2.0 to C:/PythonXX/tcl/Togl2.0
"""

import sys
import os
try:
    import tkinter
    import tkinter.filedialog as tkinter_filedialog
except ImportError as e:
    import Tkinter as tkinter
    import tkFileDialog as tkinter_filedialog
import togl
import opengl
import opengl.rokuro
import mqobuilder
import pmdbuilder
import pmxbuilder


class Frame(tkinter.Frame):
    def __init__(self, width, height, master=None, **kw):
        #super(Frame, self).__init__(master, **kw)
        tkinter.Frame.__init__(self, master, **kw)
        self.master.title('pymeshio viewer')
        self.current='.'
        # setup menu
        menu_bar = tkinter.Menu(self)
        self.master.config(menu=menu_bar)

        menu_file = tkinter.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label='File', menu=menu_file, underline=0)

        menu_file.add_command(label='Open', under=0, command=self.onOpen)

        # setup opengl widget
        self.view=opengl.rokuro.RokuroView()
        self.glworld=opengl.BaseController(self.view)
        self.glwidget=togl.Widget(self, self.glworld, width=width, height=height)
        self.glwidget.pack(fill=tkinter.BOTH, expand=True)

        # event binding
        self.bind('<Key>', self.onKeyDown)
        self.bind('<MouseWheel>', lambda e: self.glworld.onWheel(-e.delta) and self.glwidget.onDraw())

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
        self.glworld.setRoot(model)
        bb=model.get_boundingbox()
        print(bb)
        self.view.look_bb(*bb)
        self.glwidget.onDraw()

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


g_path=None
def load(path):
    global g_path
    g_path=path

def main(w, h):
    f = Frame(width=w, height=h)
    f.pack(fill=tkinter.BOTH, expand=True)
    f.focus_set()
    if g_path:
        f.load(g_path)
    f.mainloop()

if __name__ == '__main__':
    if len(sys.argv)>1:
        load(sys.argv[1])
    main(600, 600)

