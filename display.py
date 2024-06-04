import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from cube import Cube
from pyramid import Pyramid
from prism import Prism


class Display:
    def __init__(self):
        self.models = [Cube(), Pyramid(), Prism()]
        self.current_model_index = 0
        self.translation_offsets = {'x': 0, 'y': 0, 'z': 0}
        self.rotation_angles = {'x': 0, 'y': 0, 'z': 0}
        self.scaling_factors = {'x': 1, 'y': 1, 'z': 1}
        self.screen_width = 800
        self.screen_height = 600
        self.initialize_pygame()
        self.initialize_opengl()
        self.run()

    def initialize_pygame(self):
        pygame.init()
        pygame.display.set_mode((self.screen_width, self.screen_height), pygame.OPENGL | pygame.DOUBLEBUF)

    def initialize_opengl(self):
        glViewport(0, 0, self.screen_width, self.screen_height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.screen_width / self.screen_height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)

    def draw_model(self, model):
        glBegin(GL_LINES)
        for edge in model.edges:
            for vertex in edge:
                glVertex3fv(model.vertices[vertex])
        glEnd()

    def translate_obj(self, direction, amount):
        # Update translation offsets based on direction and amount
        if direction == 'x':
            self.translation_offsets['x'] += amount
        elif direction == 'y':
            self.translation_offsets['y'] += amount
        elif direction == 'z':
            self.translation_offsets['z'] += amount

    def rotate_obj(self, axis, angle):
        # Update rotation angles based on axis and angle
        self.rotation_angles[axis] += angle

    def scale_obj(self, axis, factor):
        # Update scaling factors based on axis and factor
        self.scaling_factors[axis] *= factor

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_model_index = (self.current_model_index + 1) % len(self.models)
                # Translate object based on user input
                elif event.key == pygame.K_LEFT:
                    self.translate_obj('x', -0.5)
                elif event.key == pygame.K_RIGHT:
                    self.translate_obj('x', 0.5)
                elif event.key == pygame.K_UP:
                    self.translate_obj('y', 0.5)
                elif event.key == pygame.K_DOWN:
                    self.translate_obj('y', -0.5)
                # Rotate object based on user input
                elif event.key == pygame.K_s:
                    self.rotate_obj('x', 3)
                elif event.key == pygame.K_w:
                    self.rotate_obj('x', -3)
                elif event.key == pygame.K_d:
                    self.rotate_obj('y', 3)
                elif event.key == pygame.K_a:
                    self.rotate_obj('y', -3)
                elif event.key == pygame.K_q:
                    self.rotate_obj('z', 3)
                elif event.key == pygame.K_e:
                    self.rotate_obj('z', -3)
                # Scale object based on user input
                elif event.key == pygame.K_r:
                    self.scale_obj('x', 0.9)
                elif event.key == pygame.K_f:
                    self.scale_obj('x', 1.1)
                elif event.key == pygame.K_t:
                    self.scale_obj('y', 0.9)
                elif event.key == pygame.K_g:
                    self.scale_obj('y', 1.1)
                elif event.key == pygame.K_y:
                    self.scale_obj('z', 0.9)
                elif event.key == pygame.K_h:
                    self.scale_obj('z', 1.1)

    def run(self):
        while True:
            self.handle_events()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
            glTranslatef(0, 0, -3)
            glTranslatef(self.translation_offsets['x'], self.translation_offsets['y'], self.translation_offsets['z'])
            glRotatef(self.rotation_angles['x'], 1, 0, 0)  # Rotate around x-axis
            glRotatef(self.rotation_angles['y'], 0, 1, 0)  # Rotate around y-axis
            glRotatef(self.rotation_angles['z'], 0, 0, 1)  # Rotate around z-axis
            glScalef(self.scaling_factors['x'], self.scaling_factors['y'], self.scaling_factors['z'])
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw_model(self.models[self.current_model_index])
            pygame.display.flip()
            pygame.time.wait(10)


if __name__ == "__main__":
    Display()
