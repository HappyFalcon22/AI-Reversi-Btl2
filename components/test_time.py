import pygame
import time

pygame.init()

# Set the screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the font and font size
font = pygame.font.Font(None, 36)

# Set the countdown timer duration in seconds
countdown_duration = 60

# Get the start time and end time for both timers
start_time_1 = None
end_time_1 = None
start_time_2 = None
end_time_2 = None

# Set the time remaining for both timers
time_remaining_1 = countdown_duration
time_remaining_2 = countdown_duration

# Set a flag to determine which timer is currently running
timer_running = None

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # If no timer is running, start timer 1
                if timer_running is None:
                    start_time_1 = time.time() - (countdown_duration - time_remaining_1)
                    end_time_1 = start_time_1 + countdown_duration
                    timer_running = 1
                # If timer 1 is running, stop it and start timer 2
                elif timer_running == 1:
                    timer_running = None
                    start_time_2 = time.time() - (countdown_duration - time_remaining_2)
                    end_time_2 = start_time_2 + countdown_duration
                    timer_running = 2
                # If timer 2 is running, stop it and reset the flag
                elif timer_running == 2:
                    timer_running = None
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # If timer 1 is running, calculate the time remaining and render it on the screen
    if timer_running == 1:
        time_remaining_1 = max(0, end_time_1 - time.time())
        text_1 = font.render("Timer 1: {:.2f}".format(time_remaining_1), True, (0, 0, 0))
        screen.blit(text_1, (10, 10))
    
    # If timer 2 is running, calculate the time remaining and render it on the screen
    elif timer_running == 2:
        time_remaining_2 = max(0, end_time_2 - time.time())
        text_2 = font.render("Timer 2: {:.2f}".format(time_remaining_2), True, (0, 0, 0))
        screen.blit(text_2, (10, 50))
    
    # If no timer is running, render both timers on the screen
    else:
        text_1 = font.render("Timer 1: {:.2f}".format(time_remaining_1), True, (0, 0, 0))
        screen.blit(text_1, (10, 10))
        text_2 = font.render("Timer 2: {:.2f}".format(time_remaining_2), True, (0, 0, 0))
        screen.blit(text_2, (10, 50))
    
    # Update the display
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
