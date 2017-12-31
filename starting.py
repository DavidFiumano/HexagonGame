from os import path
from gameData import GlobalGameState, Game, gameObj

class Starting:

    def __init__(self):
        self.allowed_game_settings = ['Resolution', # Resolution of the Window
                                      'Window_type', # Type of window (Borderless, Bordered)
                                      'DoubleBufferingEnabled', # True by default to prevent flickering
                                      'VSync', # disabled by default
                                      'MaxFPS', # capped at 144 by default
                                      'DepthBuffer', # 24 bits by default, no real reason to change this except (possibly) on 3d monitors
                                      'AllowMods' # Whether or not to enable mods
                                      ] # TODO, don't hardcode this. instead, draw this from some settings file



    def Read_Game_Settings(self):
        self.settings = {} # dictionary that we return
        # dictionary keys are strings indicating the setting, dictionary values are the setting (int, float, string, etc)
        settings_file = open(gameObj.game_settings_path)
        raw_settings = settings_file.read() # reads the entire file, since this is (in theory) a small file
        # yes, this means you can crash someone's game by putting a 50 GB settings file instead of the actual setting file
        raw_settings.replace(' ', '') # remove all spaces

        raw_settings_list = raw_settings.split('\n') # split settings into their constituent lines

        for setting in raw_settings_list: # remove blank lines
            if len(setting) == 0:
                raw_settings_list.remove(setting)

        for setting in raw_settings_list:
            print(setting)
            temp_setting = setting.split(':') # splits the setting between the key and it's values
            if temp_setting[0] in self.allowed_game_settings or len(temp_setting[0]) == 0: # if it's one of the allowed settings or a blank line
                if temp_setting[0] == 'Resolution':
                    self.settings[temp_setting[0]] = temp_setting[1] # these are both strings
                elif temp_setting[0] == 'Window_type':
                    self.settings[temp_setting[0]] = temp_setting[1] # these are both strings
                elif temp_setting[0] == 'DoubleBufferingEnabled':
                    self.settings[temp_setting[0]] = bool(temp_setting[1]) # convert from string to bool. Must be capital T or F in the settings file
                elif temp_setting[0] == 'VSync':
                    self.settings[temp_setting[0]] = bool(temp_setting[1]) # convert from string to bool. Must be capital T or F in the settings file
                elif temp_setting[0] == 'MaxFPS':
                    self.settings[temp_setting[0]] = int(temp_setting[1]) # convert from string to int. None of this 1/10th of a frame bullshit.
                elif temp_setting[0] == 'DepthBuffer':
                    self.settings[temp_setting[0]] = int(temp_setting[1]) # convert from string to int. No half bits!
                elif temp_setting[0] == 'AllowMods':
                    self.settings[temp_setting[0]] = bool(temp_setting[1]) # convert from string to bool
                else:
                    continue # ignore blank lines, since those aren't caught above
            else:
                print('Disallowed setting: ', temp_setting[0], ' found in settings/game.settings')

        return self.settings
