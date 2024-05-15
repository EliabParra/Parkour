from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina import Ursina, camera, window, Entity, dedent

app = Ursina(borderless=False)
random.seed(0)
window.size=(1600,800)
window.fps_counter.enabled = False
Entity.default_shader = lit_with_shadows_shader
music = Audio('/assets/music.m4a', loop=True, autoplay=True, volume = .5)

player = FirstPersonController(collider = 'box')
player.cursor.color = color.white
player.cursor.scale = .0065
player.position = Vec3(0,2,0)
class Cubo(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            scale = (1,1),
            origin_y = -.5,
            collider = 'box',
            texture = '/assets/cube_texture.png'
        )

Cubo(position=(0,1,0))
Cubo(position=(64,1,64))
Cubo(position=(-58,103,-60))
auxiliar1 = Cubo(position=(-63,2,-60))
auxiliar1.color = color.white
auxiliar1.texture = 'white_cube'
auxiliar2 = Cubo(position=(-120,0,-62))

action_active = False

def input(key):
    if key == 'escape':
        quit()
    global action_active
    if key == '`':
        action_active = not action_active
        if action_active:
            mouse.locked = False
            mouse.visible = True
        else:
            mouse.locked = True
            mouse.visible = False
    if key == 'm':
        action_active = not action_active
        if action_active:
            music.pause()
        else:
            music.resume()

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
    cubo = Cubo(position=(random.randint(-63,-55),y+2,random.randint(-63,-55)))

for x in range(75):
    cubo = Cubo(position=(x-133,random.randint(-1,2)*1.2,random.randint(-63,-60)))

for y in range(40):
    cubo = Cubo(position=(random.randint(-137,-134),(y+1)*1.2,random.randint(-63,-61)))
    if y == 39:
        cubo.color = color.green
        cubo.texture = 'white_cube'
        meta3 = cubo

ground = Entity(
    model = 'plane',
    collider = 'box',
    color = color.hsv(4,88,100,.3),
    scale = 512,
    position = Vec3(0,-50,0)
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
    if(player.position.y <= -30):
        player.position = Vec3(0,3,0)
    if player.intersects(meta1):
        player.position = Vec3(64,3,64)
        if(player.position.y <= -10):
            player.position = Vec3(64,3,64)
    if player.intersects(meta2):
        player.position = Vec3(-58,106,-60)
        if(player.position.y <= -10):
            player.position = Vec3(0,3,0)
    if player.intersects(wall):
        player.position = Vec3(-58,106,-60)
    if player.intersects(meta3):
        txt = Text(
            text = 'FELICIDADES, HAS GANADO!',
            scale = 3,
            position = (-.5,.22),
            color = color.red,
            font='VeraMono.ttf'
        )
        destroy(music)
        win_sound = Audio('assets/WIN sound effect.m4a', autoplay = True)

Sky()

app.run()