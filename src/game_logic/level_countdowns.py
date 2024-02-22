from game_logic import constants,blit_text

def level_one_countdown(elapsed_time):
    if elapsed_time <= 6:
        blit_text.display_text(constants.SCREEN,"level 1",constants.MAIN_FONT,constants.CENTRE_X,constants.CENTRE_Y,(255,0,0))
    elif elapsed_time <= 9:
        blit_text.display_text(constants.SCREEN,"5",constants.MAIN_FONT,constants.CENTRE_X,constants.CENTRE_Y,(255,0,0))