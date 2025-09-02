from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = True
window.title = 'The Water Fight'

light = DirectionalLight()
light.look_at(Vec3(1, -2, 1))
Sky()

ground = Entity(model='plane', scale=100, texture = 'white_cube', texture_scale = (50, 50), collider='box', shader=lit_with_shadows_shader)

player = FirstPersonController(model='cube', color=color.orange, scale_y=4, origin_y=-2, collider='box', speed=5, shader=lit_with_shadows_shader)
player.gravity = 0.5
player.cursor.color = color.white

water_gun = Entity(parent=camera, model='cube', color=color.blue, scale=(0.1, 0.1, 0.5), position=(0.3, -0.2, 1), rotation=(0, 90, 0), shader=lit_with_shadows_shader)

def update():
    if p

app.run()