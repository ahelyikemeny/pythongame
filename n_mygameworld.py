import pgzrun
from typing import List
import pygame
from pgzero.builtins import *


class MyActor(Actor):

    elapsed_time: float = 0
    _stage: 'MyStage' = 0
    _on_mouse_down_listener = 0
    _on_mouse_up_listener = 0
    _on_mouse_move_listener = 0
    _width: int = -1
    _height: int = -1

    def update(self, deltaTime: float = 0.0166666666666666666666):
        self.elapsed_time += deltaTime

    def overlaps_with(self, otheractor: 'MyActor') -> bool:
        return self.colliderect(otheractor)

    def overlaps_point(self, pos) -> bool:
        return self.collidepoint(pos)

    def set_on_mouse_down_listener(self, func):
        self._on_mouse_down_listener = func

    def on_mouse_down(self, pos, button):
        if self.overlaps_point(pos):
            if self._on_mouse_down_listener != 0:
                self._on_mouse_down_listener(pos, button)

    def set_on_mouse_up_listener(self, func):
        self._on_mouse_up_listener = func

    def on_mouse_up(self, pos, button):
        if self.overlaps_point(pos):
            if self._on_mouse_up_listener != 0:
                self._on_mouse_up_listener(pos, button)

    def set_on_mouse_move_listener(self, func):
        self._on_mouse_move_listener = func

    def on_mouse_move(self, pos):
        if self.overlaps_point(pos):
            if self._on_mouse_move_listener != 0:
                self._on_mouse_move_listener(pos)

    def remove_from_stage(self):
        try:
            self._stage.remove_actor(actor=self)
        except ValueError:
            print("A következő objektum már el lett távolítva korábban: " + str(id(self)))

    def remove_on_mouse_down_listener(self):
        self._on_mouse_down_listener = 0

    def remove_on_mouse_up_listener(self):
        self._on_mouse_up_listener = 0

    def remove_on_mouse_move_listener(self):
        self._on_mouse_move_listener = 0

    def set_size(self, width: int, height: int):
        if self._width == -1 or self._height == -1:
            self._surf = pygame.transform.scale(self._surf, (self.width, self.height))
        else:
            self._surf = pygame.transform.scale(self._surf, (width, height))
        self._width = width
        self._height = height
        self._update_pos()

    def set_stage(self, stage: 'MyStage'):
        self._stage = stage

    def set_rotation(self, degree: int):
        self.angle = degree
        self.set_size(self._width, self._height)

    def rotate_with(self, degree: int):
        self.set_rotation(self.angle + degree)

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_width(self, width: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(width, int(float(self._height) * (float(width) / float(self._width))))
        else:
            self.set_size(width, self._height)

    def set_height(self, height: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(int(float(self._width) * (float(height) / float(self._height))), height)
        else:
            self.set_size(self._width, height)

    def get_width(self)->int:
        return self._width

    def get_height(self)->int:
        return self._height

class MyStage:
    actors: List[MyActor]
    elapsedTime: float = 0
    _on_mouse_down_listener = 0
    _on_mouse_up_listener = 0
    _on_mouse_move_listener = 0

    def __init__(self):
        self.actors = []

    def update(self, deltaTime: float = 0.0166666666666666666666):
        self.elapsedTime += deltaTime
        for obj in self.actors:
            obj.update(deltaTime)

    def draw(self):
        for obj in self.actors:
            obj.draw()

    def add_actor(self, actor: MyActor):
        self.actors.append(actor)
        if actor._stage != 0:
            print("A következő actor át lett helyezve a " + str(id(actor._stage)) + " stageből a " + str(id(self)) + " stagebe.")
            actor.remove_from_stage()
        actor.set_stage(self)

    def remove_actor(self, actor: MyActor):
        self.actors.remove(actor)

    def on_mouse_down(self, pos, button):
        if self._on_mouse_down_listener != 0:
            self._on_mouse_down_listener(pos, button)
        for obj in self.actors:
            obj.on_mouse_down(pos, button)

    def on_mouse_up(self, pos, button):
        if self._on_mouse_up_listener != 0:
            self._on_mouse_up_listener(pos, button)
        for obj in self.actors:
            obj.on_mouse_up(pos, button)

    def on_mouse_move(self, pos):
        if self._on_mouse_move_listener != 0:
            self._on_mouse_move_listener(pos)
        for obj in self.actors:
            obj.on_mouse_move(pos)

    def remove_on_mouse_down_listener(self):
        self._on_mouse_down_listener = 0

    def remove_on_mouse_up_listener(self):
        self._on_mouse_up_listener = 0

    def remove_on_mouse_move_listener(self):
        self._on_mouse_move_listener = 0

    def set_on_mouse_down_listener(self, func):
        self._on_mouse_down_listener = func

    def set_on_mouse_up_listener(self, func):
        self._on_mouse_up_listener = func

    def set_on_mouse_move_listener(self, func):
        self._on_mouse_move_listener = func
