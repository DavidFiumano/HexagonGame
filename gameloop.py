from pyglet import *

from gameData import GlobalGameState, Game, gameObj
from starting import Starting
from menu import Menu


## STATE OBJECTS, HOW THE GAME RETRIEVES DATA/ACCESSES DATA MEMBERS FROM THESE OBJECTS ##
startingObj = Starting()
#Loading_ScreenObj = Loading_Screen()
MenuObj = Menu()
#In_GameObj = In_Game()
#Closing = Closing()
#Hard_Paused = Hard_Paused()

# WINDOW EVENTS ##
@gameObj.game_window.event
def on_draw():
    if gameObj.globalGameState == GlobalGameState.Starting:
        gameObj.set_settings(startingObj.Read_Game_Settings()) # read the settings and store them in Game()
        raw_resolution = gameObj.get_setting('Resolution').split('x') # store the setting temporarily
        formatted_resolution = (int(raw_resolution[0]), int(raw_resolution[1])) # format it, convert to int
        gameObj.game_window.set_size(formatted_resolution[0], formatted_resolution[1]) # set the resolution of the window
        gameObj.game_window.set_visible() # make the window visible
        gameObj.globalGameState = GlobalGameState.Loading_Screen
    elif gameObj.globalGameState == GlobalGameState.Loading_Screen:
        gameObj.globalGameState = GlobalGameState.Menu
    elif gameObj.globalGameState == GlobalGameState.Menu:
        MenuObj.manage_menu()
    elif gameObj.globalGameState == GlobalGameState.In_Game:
        exit()
    elif gameObj.globalGameState == GlobalGameState.Closing:
        pass


@gameObj.game_window.event
def on_deactivate():
    # when the user switches windows
    pass

@gameObj.game_window.event
def on_hide():
    # when the user minimizes the window
    pass

@gameObj.game_window.event
def on_resize(width, height):
    # when the window is resized
    pass

## KEYBOARD EVENTS ##
@gameObj.game_window.event
def on_key_press(symbol, modifiers):
    gameObj.game_window.clear()

@gameObj.game_window.event
def on_key_release(symbol, modifiers):
    # when a key is released
    pass

## MOUSE EVENTS ##
@gameObj.game_window.event
def on_mouse_press(x, y, symbol, modifiers):
    pass

@gameObj.game_window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    # whenthe mouse moves with one or more buttons pressed
    # x and y are locations
    # dx and dy are the change since the last time the function was called
    # stays active as long as the drag lasts (even if it exits the window)
    pass

@gameObj.game_window.event
def on_mouse_enter(x, y):
    # when the mouse enters the screen
    pass

@gameObj.game_window.event
def on_mouse_leave(x, y):
    # when the mouse leaves the screen
    pass

@gameObj.game_window.event
def on_mouse_motion(x, y, dx, dy):
    # when the mouse moves
    # dx and dy are the amount of change in movement
    pass

@gameObj.game_window.event
def on_mouse_scroll(x, y, dx, dy):
    # when the mouse scroll wheel is activated
    # most mice don't have an x direction, so the scroll is usually zero
    # the apple mighty mouse has an x direction though, so it's still useful I guess
    pass

## TEXT EVENTS ##

@gameObj.game_window.event
def on_text(unicode):
    # used to interpret text, since converting the keystrokes to unicode is a pain
    pass

@gameObj.game_window.event
def on_text_motion(motion):
    # when the text cursor moves
    # can take:
    # MOTION_UP
    # MOTION_RIGHT
    # MOTION_DOWN
    # MOTION_LEFT
    # MOTION_NEXT_WORD
    # MOTION_PREVIOUS_WORD
    # MOTION_BEGINNING_OF_LINE
    # MOTION_END_OF_LINE
    # MOTION_NEXT_PAGE
    # MOTION_PREVIOUS_PAGE
    # MOTION_BEGINNING_OF_FILE
    # MOTION_END_OF_FILE
    # MOTION_BACKSPACE
    # MOTION_DELETE
    pass

def on_text_motion_select(motion):
    # user highlights/selects text
    # same input as specified in on_text_motion
    pass

def start_game():
    gameObj.globalGameState = GlobalGameState(1)
    try:
        app.run()
    except Exception as e:
        print(e)

start_game()
