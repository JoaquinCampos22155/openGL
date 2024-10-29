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


#acepta pnj y jpg
faceModel = Model("models/buffalo.obj")
faceModel.AddTexture("models/textures/buffalo.bmp")
faceModel.translation.z = - 10
faceModel.scale.x = 2
faceModel.scale.y = 2
faceModel.scale.z = 2
rend.scene.append(faceModel)

isRunning = True

vShader = vertex_shader
fShader = fragment_shader
rend.SetShaders(vShader, fShader)

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
                vShader = vertex_shader
                fShader = fragment_shader
                rend.SetShaders(vShader, fShader)
            
            elif event.key == pygame.K_4:
                vShader = deflate_shader 
                rend.SetShaders(vShader, fShader)
            
            elif event.key == pygame.K_5:
                vShader = twist_shader
                rend.SetShaders(vShader, fShader)
            
            elif event.key == pygame.K_6:
                vShader = colapse_shader
                rend.SetShaders(vShader, fShader)
            
            elif event.key == pygame.K_7:
                fShader = bicolor_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_8:
                fShader = noise_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_9:
                fShader = gradient_shader
                rend.SetShaders(vShader, fShader)
            
    #model            
    if keys[K_LEFT]:
        faceModel.rotation.y -= 10 * deltaTime     
    if keys[K_RIGHT]:
        faceModel.rotation.y += 10 * deltaTime  
    if keys[K_UP]:
        faceModel.rotation.x -= 10 * deltaTime  
    if keys[K_DOWN]:
        faceModel.rotation.x += 10 * deltaTime  
    
    #camera
    if keys[K_a]:
        rend.camera.position.x -= 1* deltaTime
    if keys[K_d]:
        rend.camera.position.x += 1* deltaTime
    if keys[K_w]:
        rend.camera.position.y -= 1* deltaTime  
    if keys[K_s]:
        rend.camera.position.y += 1* deltaTime
    if keys[K_g]:
        rend.camera.position.z -= 1* deltaTime  
    if keys[K_t]:
        rend.camera.position.z += 1* deltaTime
        
    #light
    if keys[K_i]:
        rend.pointLight.x -= 1 * deltaTime
    if keys[K_p]:
        rend.pointLight.x += 1 * deltaTime
    if keys[K_l]:
        rend.pointLight.y -= 1 * deltaTime
    if keys[K_o]:
        rend.pointLight.y += 1 * deltaTime
    if keys[K_i]:
        rend.pointLight.x -= 1 * deltaTime
    if keys[K_p]:
        rend.pointLight.x += 1 * deltaTime
    if keys[K_k]:
        rend.pointLight.z -= 1 * deltaTime
    if keys[K_m]:
        rend.pointLight.z += 1 * deltaTime
        
    rend.time += deltaTime       
    
    rend.camera.LookAt(faceModel.translation)
    
    rend.Render()
    pygame.display.flip()	  

pygame.quit()  
  
