import pygame
from pygame.locals import * 
from gl import Renderer
from shaders import *
from model import *
width = 960
height = 540

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen) 

rend.SetShaders(vertex_shader, fragment_shader)

#acepta pnj y jpg
faceModel = Model("models/face.obj")
faceModel.AddTexture("models/textures/model.bmp")
faceModel.translation.z = - 5
faceModel.scale.x = 2
faceModel.scale.y = 2
faceModel.scale.z = 2
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
            elif event.key == pygame.K_3:
                rend.SetShaders(vertex_shader, fragment_shader)
            elif event.key == pygame.K_4:
                rend.SetShaders(fat_shader, fragment_shader)
            elif event.key == pygame.K_5:
                rend.SetShaders(water_shader, fragment_shader)
                
    if keys[K_LEFT]:
        faceModel.rotation.y -= 10 * deltaTime     
    if keys[K_RIGHT]:
        faceModel.rotation.y += 10 * deltaTime  
    if keys[K_UP]:
        faceModel.rotation.x -= 10 * deltaTime  
    if keys[K_DOWN]:
        faceModel.rotation.x += 10 * deltaTime  
    
    if keys[K_a]:
        rend.camera.position.x -= 1* deltaTime
    if keys[K_d]:
        rend.camera.position.x += 1* deltaTime
    if keys[K_w]:
        rend.camera.position.y -= 1* deltaTime  
    if keys[K_s]:
        rend.camera.position.y += 1* deltaTime
    rend.time += deltaTime       
    
    rend.camera.LookAt(faceModel.translation)
    
    rend.Render()
    pygame.display.flip()	  

pygame.quit()  
  
