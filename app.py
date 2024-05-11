from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)
random.seed(0)
window.size=(1000,600)
Entity.default_shader = lit_with_shadows_shader

player = FirstPersonController(collider = 'box')

initialPosition = Vec3(0,5,0)

class Cubo(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            scale = (1,1),
            origin_y = -.5,
            color = color.violet,
            collider = 'box',
            texture = 'white_cube',
        )
        
Cubo(position=(0,1,0))
Cubo(position=(64,1,64))
Cubo(position=(-64,1,-64))

player.position = Vec3(0,2,0)

def input(key):
    if key == 'escape':
        quit()
    if key == '`':
        mouse.locked = False
        mouse.visible = True
    if key == 'control':
        mouse.locked = True
        mouse.visible = False
        
for z in range(47):
    cubo = Cubo(position=(random.randint(-2,2),random.randint(-1,3),z+2))
    if z == 46:
        cubo.color = color.green
        meta1 = cubo

    # cubo = Cubo(position=(-64,1,z))
        
for y in range(40):
    cubo = Cubo(position=(random.randint(63,66),(y+1)*1.2,random.randint(62,65)))
    if y == 39:
        cubo.color = color.green
        meta2 = cubo

for x in range(40):
    cubo = Cubo(position=(random.randint(63,66),(y+1)*1.2,random.randint(62,65)))
    if y == 39:
        cubo.color = color.green
        meta2 = cubo


for x in range(40):
    cubo = Cubo(position=((x-56)*1.1,random.randint(1,4),))

ground = Entity(
    model = 'plane',
    collider = 'box',
    color = color.red,
    scale = 256
)
ground.position = Vec3(0,-20,0)

def update():
    if(player.position.y <= -10):
        player.position = Vec3(-64,3,-64)
    if player.intersects(meta1):
        player.position = Vec3(64,3,64)
    if player.intersects(meta2):
        player.position = Vec3(64,1,64)

Sky()

app.run()