import pygame
from pygame.locals import * 
from gl import Renderer
from shaders import *
from model import *
width = 800
height = 800

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen) 
# rend.SetShaders(vertex_shader, fragment_shader)


#acepta pnj y jpg
faceModel = Model("models/face.obj")
faceModel.AddTexture("models/model.bmp")
faceModel.rotation.y = 180
rend.scene.append(faceModel)
isRunning = True

while isRunning:
    deltaTime = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_1:
                rend.FilledMode()
            elif event.key == pygame.K_2:
                rend.WireframeMode()
                
    if keys[K_LEFT]:
        faceModel.rotation.y -= 10 * deltaTime     
    if keys[K_RIGHT]:
        faceModel.rotation.y += 10 * deltaTime  
    if keys[K_UP]:
        faceModel.rotation.x -= 10 * deltaTime  
    if keys[K_DOWN]:
        faceModel.rotation.x += 10 * deltaTime  
    
    rend.time += deltaTime       
    # print(deltaTime)
    rend.Render()
    pygame.display.flip()	  

pygame.quit()  
  
