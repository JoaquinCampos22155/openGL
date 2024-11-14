# openGL

# Proyecto OpenGL con Pygame

Este proyecto usa **OpenGL** y **Pygame** que permite la carga, renderización y manipulación de modelos 3D. El objetivo principal de este proyecto es proporcionar una experiencia interactiva donde el usuario puede explorar modelos 3D con distintas configuraciones y efectos visuales
- FELICIDADES CARLOS EN SU BODA 🥳 🥳 🥳

## Contexto
- **Espacio**: a lo largo del universo nos podemos encontrar con muchas cosas inesperadas, en este caso un jumpscare no sera suficiente, presione la tecla *ESPACIO* para recorrer la lista de modelos con sus respectivos shaders.

## Controles
Para hacerlo lo mas fácil posible nos enfocaremos en espacio movimiento de mouse + click izquierdo, espacio, 1 y flechas como controles.
- CLICKSOSTENIDO + MOUSE: este permite hacer los movimientos de cámara como girar alrededor del modelo actual.
- ESPACIO: nos premite cambiar de modelo, shaders, y sonidos dentro del escenario
- 1: lo estamos usando para resetear los shaders, en caso querramos ver un modelo sin la necesidad de ver el shader podemos presionar 1 y el shader sera el vertex y fragment.
- flechas: controles para la luz, en nuestro caso tenemos el sol enfrente de nuestros modelos por lo que podemos ver que al mover la luz puntual es minimo el cambio pero se invita a experimentar.
- CONTROLES EXTRA: dentro del codigo podemos ver otros controles como wasd y otros los cuales son poco relevantes pero tambien se invita a experimentar en caso se desee.

## Características

- **Modelos 3D**: Carga y visualización de varios modelos 3D, como alienígenas, búfalos y planetas.
- **Texturas**: Los modelos pueden tener múltiples texturas aplicadas.
- **Shaders**: El usuario puede aplicar diferentes shaders de vértices y fragmentos para alterar el aspecto visual de los modelos.
- **Sonidos**: Se reproducen sonidos correspondientes a los modelos que se visualizan.
- **Cámara**: Control total sobre la cámara para explorar la escena desde diferentes ángulos y distancias.
- **Iluminación**: Posibilidad de mover una luz puntual en la escena.

## Requisitos
# USAR BRANCH DE PROYECTOFINAL
Para ejecutar este proyecto, necesitarás tener instalados los siguientes paquetes:

- `pygame`
- `PyOpenGL`

Puedes instalarlos usando `pip`:

```bash
pip install pygame PyOpenGL
