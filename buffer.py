import glm #pip install PyGLM
from numpy import array, float32
#pip install PyOpenGL
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class Buffer(object):
    def __init__(self, data):
        self.vertBuffer = array(data, float32)
        
        #Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        
        # Vertex Array Object 
        self.VAO = glGenVertexArrays(1)
        
    def Render(self):
        #atar buffer a tarjeta
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)
        
        # mandar info de verts
        glBufferData(GL_ARRAY_BUFFER, #BUFFER ID 
                     self.vertBuffer.nbytes,# buffer size in bytes
                     self.vertBuffer, # buffer data
                     GL_STATIC_DRAW) #usage
        
        # atributos
        
        # atributo pos
        glVertexAttribPointer(0, # attribute number
                              3, # size
                              GL_FLOAT, # type
                              GL_FALSE, # is normalized
                              4 * 8, # Stride size in bytes
                              ctypes.c_void_p(0)) # Offset 
        
        glEnableVertexAttribArray(0)
        #atributo coords tex
        glVertexAttribPointer(1, # attribute number
                              2, # size
                              GL_FLOAT, # type
                              GL_FALSE, # is normalized
                              4 * 8, # Stride size in bytes
                              ctypes.c_void_p(4*3)) # Offset 
        
        glEnableVertexAttribArray(1)
        #atributo normales
        glVertexAttribPointer(2, # attribute number
                              3, # size
                              GL_FLOAT, # type
                              GL_FALSE, # is normalized
                              4 * 8, # Stride size in bytes
                              ctypes.c_void_p(4*5)) # Offset 
        
        glEnableVertexAttribArray(2)
        
        glDrawArrays(GL_TRIANGLES, 0, int(len(self.vertBuffer) / 8))
        