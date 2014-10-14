#!/usr/bin/env python

import os
import pygame
import sys
import time
import traceback
import GIFImage

from pygame.locals import *

SCREEN_SIZE = (-1, -1)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
sound_key_mappings = {
    pygame.K_b : "batman.mp3",
    pygame.K_h : "hacker.mp3",
    pygame.K_i : "inception.mp3",
    pygame.K_m : "milhouse.mp3",
    pygame.K_o : "doh.mp3",
    pygame.K_s : "trombone.ogg",
    pygame.K_t : "trap.mp3",
    pygame.K_w : "woohoo.mp3"
    }
gif_key_mappings = {
    pygame.K_r : "sideshow_bob.gif",
    pygame.K_t : "ackbar.gif",
    pygame.K_d : "thisisdog.gif",
    pygame.K_m : "milhouse.gif",
    }
img_key_mappings = {
    pygame.K_n : "noideadog.jpg"
    }

loaded_gifs = { }

loaded_imgs = { }

def pathof(file):
    return os.path.join(os.path.dirname(__file__), file)

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    SCREEN_SIZE = (infoObject.current_w, infoObject.current_h)
    surface = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)
    pygame.display.set_caption("Cliff Soundboard")
    pygame.mixer.init()
    running = True
    gif = None
    img = None
    while running:
        surface.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and bool(event.mod & pygame.KMOD_ALT):
                    running = False
                    
                if event.key == pygame.K_ESCAPE:
                    gif = None
                    img = None
                    pygame.mixer.music.stop()
                    
                sound = sound_key_mappings.get(event.key)
                if sound != None:
                    pygame.mixer.music.load(pathof(sound))
                    pygame.mixer.music.play()
                    
                gif_file = gif_key_mappings.get(event.key)
                if gif_file != None:
                    img = None
                    gif = loaded_gifs.get(gif_file)
                    if gif == None:
                        gif = GIFImage.GIFImage(pathof(gif_file), surface.get_size())
                        loaded_gifs[gif_file] = gif
                
                img_file = img_key_mappings.get(event.key)
                if img_file != None:
                    gif = None
                    img = loaded_imgs.get(img_file)
                    if img == None:
                        img = pygame.image.load(pathof(img_file))
                        img = pygame.transform.smoothscale(img,surface.get_size())
                        loaded_imgs[img_file] = img
        if gif != None:
            gif.render(surface, (0,0))
        if img != None:
            surface.blit(img, (0,0))
        pygame.display.flip()
        time.sleep(.033)

if __name__ == "__main__":
    try:
        main()
    except Exception, e:
        tb = sys.exc_info()[2]
        traceback.print_exception(e.__class__, e, tb)
    pygame.quit()
