from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina import Ursina, camera, window, Entity

app = Ursina(borderless=False)
random.seed(0)
window.size=(1600,800)
window.fps_counter.enabled = False
Entity.default_shader = lit_with_shadows_shader


player = FirstPersonController(collider = 'box')
player.cursor.color = color.white
player.cursor.scale = .0065

initialPosition = Vec3(0,5,0)

class Cubo(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            scale = (1,1),
            origin_y = -.5,
            collider = 'box',
            texture = '/assets/pixelcut-export (3).jpeg',
        )
        
Cubo(position=(0,1,0))
Cubo(position=(64,1,64))
Cubo(position=(-64,100,-64))

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
        cubo.texture = 'white_cube'
        meta1 = cubo
        
for y in range(40):
    cubo = Cubo(position=(random.randint(63,66),(y+1)*1.2,random.randint(62,65)))
    if y == 39:
        cubo.color = color.green
        cubo.texture = 'white_cube'
        meta2 = cubo

for y in range(100):
    cubo = Cubo(position=(random.randint(-63,-57),-y+102,random.randint(-63,-57)))
    
for x in range(35):
    cubo = Cubo(position=(x-100,random.randint(-1,3),random.randint(-62,-58)))

meta3 = Cubo(position=(-100,0,-64))
meta3.color = color.green
cubo.texture = 'white_cube'

ground = Entity(
    model = 'plane',
    collider = 'box',
    color = color.hsv(4,88,100,.3),
    scale = 256,
    position = Vec3(0,-20,0)
)

wall = Entity(
    model = 'cube',
    collider = 'box',
    color = color.hsv(4,88,100,.5),
    scale = (10,100,1),
    position = Vec3(-65,60,-60),
    texture = 'white_cube',
    rotation_y = 90
)

def update():
    if(player.position.y <= -10):
        # player.position = Vec3(0,3,0)
        player.position = Vec3(-64,103,-64)
    if player.intersects(meta1):
        player.position = Vec3(64,3,64)
    if player.intersects(meta2):
        player.position = Vec3(-64,100,-64)
    if player.intersects(wall):
        player.position = Vec3(-64,100,-64)
    if player.intersects(meta3):
        window.color = color.hsv(0, 0, .1)
        Button.default_color = color._20
        window.color = color._25\

Sky()

app.run()