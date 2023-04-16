import pygame
import os
import board
import time



def run_game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.init()

    surface = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Othello')

    table = board.Board()
    running = True
    player = -1

    positions = None  # valid positions for the human player
    last_position = None  # position of red dot

    player_time = 60
    AI_time = 60
    # start_time_player = time.time() - (60 - player_time)     #player go first, so first mark start time
    # end_time_player = start_time_player + 60
    # #start_time_AI = time.time() - (60 - AI_time)
    # end_time_AI = 0

    start_time_player = None
    end_time_player = None
    start_time_AI = None
    end_time_AI = None
    timer_running = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if player == -1:
                start_time_player = time.time() - (60 - player_time)
                end_time_player = start_time_player + 60
                timer_running = -1
            elif player == 1:
                start_time_AI = time.time() - (60 - AI_time)
                end_time_AI = start_time_AI + 60
                timer_running = 1


            if not table.is_final():
                if player == -1:
                    # The turn of the human player
                    positions = table.generate_possible_moves(player, None, False)
                    if len(positions) != 0:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos_x, pos_y = pygame.mouse.get_pos()
                            pos_x //= 100
                            pos_y //= 100
                            if (pos_y, pos_x) in positions:
                                table.set_move(pos_y, pos_x, player)
                                player = 1
                                last_position = (pos_y, pos_x)
                                positions.clear()
                    else:
                        player = 1
                        continue
                else:
                    # The turn of the computer
                    last_position = table.alpha_beta_strategy()
                    player = -1
                    if last_position is None:
                        continue
            else:
                running = False

            surface.fill((255, 255, 255))
            board.draw_table(surface)
            table.draw(surface, last_position)

            if len(positions) > 0:
                board.draw_possible_moves(surface, positions)

            pygame.display.update()
        
        if timer_running == -1:
            player_time = end_time_player - time.time()
            print("player:",player_time)
        elif timer_running == 1:
            AI_time = end_time_AI - time.time()
            print("AI", AI_time)
        
        if player_time <= 0:
            print("Player time out!!\n AI won.")
            running = False
        elif AI_time <= 0:
            print("AI time out!!\n You won.")
            running = False

if __name__ == '__main__':
    run_game()
