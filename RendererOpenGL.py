import pygame
from pygame.locals import *

from gl import Renderer
from model import Model
from shaders import *

width = 1280
height = 720

pygame.init()

screen = pygame.display.set_mode((width,height), pygame.OPENGL | pygame.DOUBLEBUF )
clock = pygame.time.Clock()

rend = Renderer(screen)

skyboxTextures = ["skybox/right.png",
				  "skybox/left.png",
				  "skybox/top.png",
				  "skybox/bottom.png",
				  "skybox/front.png",
				  "skybox/back.png"]

rend.CreateSkybox(skyboxTextures)

alienModel = Model("models/alien.obj")
alienModel.AddTexture("models/textures/alien.jpg")
alienModel.AddTexture("models/textures/alienbump.jpg")
alienModel.translation.z = -5
alienModel.scale.x = 2
alienModel.scale.y = 2
alienModel.scale.z = 2

buffaloModel = Model("models/buffalo.obj")
buffaloModel.AddTexture("models/textures/Buffalo2.png")
buffaloModel.AddTexture("models/textures/Buffalo3.png")
buffaloModel.AddTexture("models/textures/Buffalo4.png")
buffaloModel.AddTexture("models/textures/Buffalo1.png")
buffaloModel.translation.z = -20
buffaloModel.rotation.z = -80
buffaloModel.rotation.y = 30
buffaloModel.scale.x = 1
buffaloModel.scale.y = 1
buffaloModel.scale.z = 1
buffaloModel.visible = False


alien2 = Model("models/alien2.obj")
alien2.AddTexture("models/textures/alien21.jpg")
alien2.AddTexture("models/textures/alien22.jpg")
alien2.translation.z = -5
alien2.translation.y = -2
alien2.rotation.y = 0
alien2.scale.x = 0.01
alien2.scale.y = 0.01
alien2.scale.z = 0.01
alien2.visible = False


planets = Model("models/planet.obj")
planets.AddTexture("models/textures/planetas/3.png")
planets.translation.z = -10
planets.rotation.y = 0
planets.rotation.x = 0
planets.scale.x = 0.5
planets.scale.y = 0.5
planets.scale.z = 0.5
planets.visible = False

models = [alienModel, buffaloModel, alien2, planets]

rend.scene.append(alienModel)
rend.scene.append(buffaloModel)
rend.scene.append(alien2)
rend.scene.append(planets)



vShader = vertex_shader
fShader = fragment_shader

camDistance = 5
camAngle = 0
camAngleY = 0


modelIndex = 0
vshaders = [twist_shader,colapse_shader,deflate_shader,pulseripple_shader]
fShaders = [negative_shader, bicolor_shader, gradient_shader, noise_shader]
rend.SetShaders(vShader, fShader)

isRunning = True
sound4 = pygame.mixer.Sound("sonidos/ruidoradio.ogg")
sound2 = pygame.mixer.Sound("sonidos/ruidobuffalo.ogg")
sound3 = pygame.mixer.Sound("sonidos/demogorgsound.ogg")
sound1 = pygame.mixer.Sound("sonidos/aliensound.ogg")
sounds = [sound1, sound2, sound3, sound4]
current_sound = None
while isRunning:
	
	deltaTime = clock.tick(60) / 1000
	
	keys = pygame.key.get_pressed()
	mouseVel = pygame.mouse.get_rel()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
			
		elif event.type == pygame.MOUSEWHEEL:

			if event.y < 0 and camDistance < 10:
				camDistance -= event.y * deltaTime * 10

			if event.y > 0 and camDistance > 2:
				camDistance -= event.y * deltaTime * 10
				
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[2]:
				modelIndex += 1
				modelIndex %= len(rend.scene)
				for i in range(len(rend.scene)):
					rend.scene[i].visible = i == modelIndex
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				isRunning = False
			#USAR ESPACIO PARA MIRAR A DIFERENTE MODELO Y SUS SHADEERS Y SONIDOS	
			elif event.key == pygame.K_SPACE:
				camDistance = 5
				camAngle = 0
				modelIndex = (modelIndex + 1) % len(models)
				for i, model in enumerate(models):
					#modelos
					model.visible = (i == modelIndex)
					#shaders
					rend.SetShaders(vshaders[modelIndex], fShaders[modelIndex])
     				#sonidos
					if pygame.mixer.get_busy():
						pygame.mixer.stop()
					current_sound = sounds[modelIndex]
					current_sound.play()
						
				
			# reset vertex Shaders
			elif event.key == pygame.K_1:
				vShader = vertex_shader
				rend.SetShaders(vShader, fShader)

   			# reset fragment Shaders
			elif event.key == pygame.K_6:
				fShader = fragment_shader
				rend.SetShaders(vShader, fShader)			


	if keys[K_LEFT]:
		rend.pointLight.x -= 1 * deltaTime
		
	if keys[K_RIGHT]:
		rend.pointLight.x += 1 * deltaTime
		
	if keys[K_UP]:
		rend.pointLight.z -= 1 * deltaTime
		
	if keys[K_DOWN]:
		rend.pointLight.z += 1 * deltaTime
		
	if keys[K_m]:
		rend.pointLight.y += 1 * deltaTime
		
	if keys[K_n]:
		rend.pointLight.y -= 1 * deltaTime
		
	#BOTONES MOVIMIENTOS DE CAMARA
	if keys[K_a]:
		camAngle -= 45 * deltaTime
		
	if keys[K_d]:
		camAngle += 45 * deltaTime
		
	if keys[K_w]:
		if camDistance > 2:
			camDistance -= 2 * deltaTime
		
	if keys[K_s]:
		if camDistance < 10:
			camDistance += 2 * deltaTime
			
	if keys[K_q]:
		if rend.camera.position.y < 2:
			rend.camera.position.y += 5 * deltaTime
		
	if keys[K_e]:
		if rend.camera.position.y > -2:
			rend.camera.position.y -= 5 * deltaTime
			
	#MOVIMIENTOS DE CAMARA CON MOUSE
	if pygame.mouse.get_pressed()[0]:
		camAngle -= mouseVel[0] * deltaTime * 5
		
		if mouseVel[1] > 0 and rend.camera.position.y < 2:
			rend.camera.position.y += mouseVel[1] * deltaTime
			
		if mouseVel[1] < 0 and rend.camera.position.y > -2:
			rend.camera.position.y += mouseVel[1] * deltaTime
				
	model_translation = models[modelIndex].translation
	rend.camera.Orbit(model_translation, camDistance, camAngle)
	rend.camera.LookAt(model_translation)

	rend.Render()

	rend.time += deltaTime
	pygame.display.flip()
	
pygame.quit()
