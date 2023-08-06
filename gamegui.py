# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame
from pygame.locals import *
from minesweeper import sprites
import game
from game import board_visible, populate_board, reveal
win = 0
two_thousand = sprites.TileSheets(sprites.TileSheets.two_thousand)

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 288
WINDOW_WIDTH = 240
SCREEN = 0
CLOCK = 0

lost = False

def click(pos, button):
  global lost
  x = pos[0]//16
  y = pos[1]//16

  if button == 3:
    if board_visible[x][y] == None:
      board_visible[x][y] = -1
    elif board_visible[x][y] == -1:
      board_visible[x][y] = None
    return
  
  elif board_visible[x][y] != -1:
    reveal(x,y)
    if board_visible[x][y] == "*":
      lost = True

def draw(screen):
  global lost
  blit = lambda img, idx, row: screen.blit(img, (16 * idx, row * 16))
  builder = sprites.TileBuilder(two_thousand)
  builder.unopened(two_thousand).empty(two_thousand).flag(two_thousand)
  builder.question_mark(two_thousand).question_mark_click(two_thousand)
  builder.mine(two_thousand).mine_red(two_thousand).mine_red_cross(two_thousand)
  tile = builder.build()
  
  # Redraw screen here.
  blockSize = 1 #Set the size of the grid block
  for x in range(0, WINDOW_WIDTH//16, blockSize):
    for y in range(0, WINDOW_HEIGHT//16, blockSize):
      blit(tile.unopened,x,y)
  if lost:
    game.board_visible = game.board
    
  for x in range(0, WINDOW_WIDTH//16, blockSize):
    for y in range(0, WINDOW_HEIGHT//16, blockSize):
      if board_visible[x][y] == None:
        blit(tile.unopened,x,y)
      elif board_visible[x][y] == "*":
        blit(tile.mine,x,y)
      elif board_visible[x][y] == 0:
        blit(tile.empty,x,y)
      elif board_visible[x][y] == 1:
        blit(tile.one,x,y)
      elif board_visible[x][y] == 2:
        blit(tile.two,x,y)
      elif board_visible[x][y] == 3:
        blit(tile.three,x,y)
      elif board_visible[x][y] == 4:
        blit(tile.four,x,y)
      elif board_visible[x][y] == 5:
        blit(tile.five,x,y)
      elif board_visible[x][y] == 6:
        blit(tile.six,x,y)
      elif board_visible[x][y] == 7:
        blit(tile.seven,x,y)
      elif board_visible[x][y] == 8:
        blit(tile.eight,x,y)
      elif board_visible[x][y] == -1:
        blit(tile.flag,x,y)
  if lost:
    blit(lose, 1, 2)
  if game.win_check(board_visible):
    blit(win, 1, 2)
      
      # rect = pygame.Rect(x, y, blockSize, blockSize)
      # pygame.draw.rect(SCREEN, WHITE, rect, 1)
  # Flip the display so that the things we drew actually show up.
 
def runPyGame():
  global SCREEN, CLOCK, win, lose
  # Initialise PyGame.
  pygame.init()
  
  populate_board(game.board, 30)
  game.calculate_numbers(game.board)
  SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
  win = pygame.image.load("win.png").convert()
  win = pygame.transform.scale(win, (208, 150))
  lose = pygame.image.load("lost.png").convert()
  lose = pygame.transform.scale(lose, (208, 150))
  
  SCREEN.fill(BLACK)

  # Set up the window.
  
  # screen is the surface representing the window.
  # PyGame surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Main game loop.
  while True: # Loop forever!
    draw(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        click(pos, event.button)

    pygame.display.update()

runPyGame()

        


