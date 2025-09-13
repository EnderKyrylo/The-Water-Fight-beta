import os
import sys
from panda3d.core import load_prc_file

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temporary folder
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

config_file = resource_path("config.prc")
load_prc_file(config_file)


from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

development_mode = True # Set to True for production
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = True
window.title = 'The Water Fight'

light = DirectionalLight()
light.shadow_map_resolution = (8192, 8192)

light.look_at(Vec3(1, -2, 1))
Sky()

ground = Entity(model='plane', scale=100, texture = 'white_cube', texture_scale = (50, 50), collider='box', shader=lit_with_shadows_shader)

player = FirstPersonController(model='cube',collider='box', shader=lit_with_shadows_shader)
player.cursor.color = color.white

water_gun = Entity(parent=camera, model='cube', color=color.blue, scale=(0.5, 0.2, 0.2), position=(0.3, -0.2, 0.6), rotation=(0, 90, 0), shader=lit_with_shadows_shader)

def input(key):
    if key == 'escape':
        application.quit()
    

app.run()

