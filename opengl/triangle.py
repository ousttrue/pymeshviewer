# coding: utf-8
from OpenGL.GL import *


class Triangle(object):
    def __init__(self, size):
        self.size=size

    def draw(self):
        # �O�p�`�`��J�n
        glBegin(GL_TRIANGLES)
        # ����
        glVertex(-self.size, -self.size)
        # �E��
        glVertex(self.size, -self.size)
        # ��
        glVertex(0, self.size)
        # �O�p�`�`��I��
        glEnd()

