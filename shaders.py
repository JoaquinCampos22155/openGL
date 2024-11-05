
vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals; 
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;   
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    outPosition = modelMatrix * vec4(position, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;

    outTexCoords = texCoords;
    outNormals= normals;
}
'''
skybox_vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 inPosition;

out vec3 texCoords;

uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    texCoords = inPosition;
    gl_Position = projectionMatrix * viewMatrix * vec4(inPosition, 1.0);
}

'''

fat_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals; 
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    outPosition = modelMatrix * vec4(position + normals * sin(time) / 10, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals= normals;
}
'''


water_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals; 
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    outPosition = modelMatrix * vec4(position + vec3(0,1,0) * sin(time * position.x * 5) / 10, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals= normals;
}
'''
deflate_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals; 
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    float collapseFactor = abs(sin(time * 0.8)); 

    vec3 collapsedPosition = vec3(position.x, position.y * collapseFactor, position.z);

    outPosition = modelMatrix * vec4(collapsedPosition, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;

    outTexCoords = texCoords;
    outNormals = normals;
}

'''
twist_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals; 
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    float angle = sin(time + position.y) * 0.5;
    mat3 rotation = mat3(cos(angle), 0, sin(angle), 0, 1, 0, -sin(angle), 0, cos(angle));
    vec3 twistedPosition = rotation * position;
    outPosition = modelMatrix * vec4(twistedPosition, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    outTexCoords = texCoords;
    outNormals = normals;
}

'''

colapse_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

out vec2 outTexCoords;
out vec3 outNormals; 
out vec4 outPosition;

uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    float scale = 1.0 + 0.1 * sin(time * 2.0);
    vec3 scaledPosition = position * scale;

    outPosition = modelMatrix * vec4(scaledPosition, 1.0);
    gl_Position = projectionMatrix * viewMatrix * outPosition;
    
    outTexCoords = texCoords;
    outNormals = normals;
}

'''


fragment_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;
uniform vec3 pointLight;

out vec4 fragColor;

void main()
{
    float intensity = dot(outNormals, normalize(pointLight - outPosition.xyz));
    fragColor = texture(tex, outTexCoords) * intensity;
}
''' 

skybox_fragment_shader = '''
#version 450 core

uniform samplerCube skybox;

in vec3 texCoords;

out vec4 fragColor;

void main()
{
    fragColor = texture(skybox, texCoords);
} 

'''
negative_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;

out vec4 fragColor;

void main()
{
    fragColor = 1- (texture(tex, outTexCoords));
}
'''

bicolor_shader = '''

#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

out vec4 fragColor;

void main()
{
    float gradient = smoothstep(0.0, 1.0, sin(outPosition.y * 5.0) * 0.5 + 0.5);
    fragColor = vec4(gradient * 0.8, 0.3 * (1.0 - gradient), gradient, 1.0); 
}
'''

noise_shader = '''
#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

uniform sampler2D tex;
uniform float time;
out vec4 fragColor;

float random(vec2 p) {
    return fract(sin(dot(p.xy, vec2(12.9898, 78.233))) * 43758.5453123);
}

void main()
{
    vec4 color = texture(tex, outTexCoords);
    float noise = random(outPosition.xy * time) * 0.5;
    fragColor = color + vec4(vec3(noise), 0.0);
}

'''
gradient_shader = '''

#version 450 core

in vec2 outTexCoords;
in vec3 outNormals;
in vec4 outPosition;

out vec4 fragColor;
uniform sampler2D tex;
vec4 textureColor = texture(tex, outTexCoords);
uniform float time;

void main()
{
    float gradient = (outPosition.y + sin(time * 10.0)) * 0.5 + 0.5;
    fragColor = mix(textureColor, vec4(gradient, gradient * 0.5, 1.0 - gradient, 1.0), 0.5);

}
'''