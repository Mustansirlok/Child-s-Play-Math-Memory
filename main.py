import pygame
import sys
import random

pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Educational Math Games for Kids')

# Colors
BLACK = (0, 0, 0)
COTTON_CANDY = (255, 188, 217)  # Cotton Candy color (for dark purple)
SKY_BLUE = (135, 206, 235)      # Sky Blue color (for dark blue)
WHITE = (255, 255, 255)
WRONG_COLOR = (255, 0, 0)       # Red for wrong selection

# Fonts
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 50)

# Game states
MAIN_MENU = 'main_menu'
MATH_QUIZ = 'math_quiz'
MATH_MEMORY = 'math_memory'
ARITHMETIC_SEQUENCE = 'arithmetic_sequence'

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text('Math Games', font_large, COTTON_CANDY, screen, screen_width // 2, 100)
        draw_text('1. Math Quiz', font_small, SKY_BLUE, screen, screen_width // 2, 250)
        draw_text('2. Math Memory', font_small, SKY_BLUE, screen, screen_width // 2, 350)
        draw_text('3. Arithmetic Sequence', font_small, SKY_BLUE, screen, screen_width // 2, 450)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return MATH_QUIZ
                if event.key == pygame.K_2:
                    return MATH_MEMORY
                if event.key == pygame.K_3:
                    return ARITHMETIC_SEQUENCE

def math_quiz(screen):
    correct_answers = 0
    total_questions = 5

    for _ in range(total_questions):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '+':
            answer = num1 + num2
        elif operation == '-':
            answer = num1 - num2
        elif operation == '*':
            num1 = random.randint(1, 5)  # Limit multiplication to smaller numbers for simplicity
            num2 = random.randint(1, 5)
            answer = num1 * num2
        elif operation == '/':
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            num1, num2 = sorted([num1, num2], reverse=True)  # Ensure division is valid and result is integer
            answer = num1 // num2
        
        user_answer = ""
        answered = False

        while not answered:
            screen.fill(BLACK)
            draw_text(f"Question {_ + 1}/{total_questions}", font_small, SKY_BLUE, screen, screen_width // 2, 50)
            draw_text(f"{num1} {operation} {num2} = ?", font_large, COTTON_CANDY, screen, screen_width // 2, 200)
            draw_text(user_answer, font_large, COTTON_CANDY, screen, screen_width // 2, 300)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if user_answer.isdigit():
                            if int(user_answer) == answer:
                                correct_answers += 1
                            answered = True
                    elif event.key == pygame.K_BACKSPACE:
                        user_answer = user_answer[:-1]
                    else:
                        if event.unicode.isdigit():
                            user_answer += event.unicode

    screen.fill(BLACK)
    draw_text(f"Quiz Complete!", font_large, COTTON_CANDY, screen, screen_width // 2, 200)
    draw_text(f"Score: {correct_answers}/{total_questions}", font_large, COTTON_CANDY, screen, screen_width // 2, 300)
    pygame.display.flip()
    pygame.time.wait(3000)

def math_memory(screen):
    sequence = [random.randint(1, 9) for _ in range(5)]
    user_sequence = []

    screen.fill(BLACK)
    draw_text('Remember this sequence:', font_large, COTTON_CANDY, screen, screen_width // 2, 100)
    draw_text(' '.join(map(str, sequence)), font_large, COTTON_CANDY, screen, screen_width // 2, 300)
    pygame.display.flip()
    pygame.time.wait(3000)

    while True:
        screen.fill(BLACK)
        draw_text('Enter the sequence:', font_large, COTTON_CANDY, screen, screen_width // 2, 100)
        draw_text(' '.join(map(str, user_sequence)), font_large, COTTON_CANDY, screen, screen_width // 2, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    break
                elif event.key == pygame.K_BACKSPACE:
                    user_sequence = user_sequence[:-1]
                elif event.unicode.isdigit():
                    user_sequence.append(int(event.unicode))
                    if len(user_sequence) == len(sequence):
                        break

        pygame.display.flip()

        if len(user_sequence) == len(sequence):
            break

    if user_sequence == sequence:
        screen.fill(BLACK)
        draw_text('Correct!', font_large, COTTON_CANDY, screen, screen_width // 2, 300)
    else:
        screen.fill(BLACK)
        draw_text('Wrong!', font_large, COTTON_CANDY, screen, screen_width // 2, 300)

    pygame.display.flip()
    pygame.time.wait(3000)

def arithmetic_sequence(screen):
    while True:
        # Generate an arithmetic sequence with a missing number
        start = random.randint(1, 10)
        diff = random.randint(1, 5)
        sequence = [start + diff * i for i in range(5)]
        missing_index = random.randint(1, 3)
        correct_answer = sequence[missing_index]
        sequence[missing_index] = "?"

        choices = [correct_answer] + [random.randint(start, start + diff * 6) for _ in range(3)]
        random.shuffle(choices)

        selected_choice = None

        while selected_choice is None:
            screen.fill(BLACK)
            draw_text("Complete the sequence:", font_small, COTTON_CANDY, screen, screen_width // 2, 100)
            sequence_text = " ".join(map(str, sequence))
            draw_text(sequence_text, font_large, COTTON_CANDY, screen, screen_width // 2, 200)

            for i, choice in enumerate(choices):
                draw_text(str(choice), font_small, SKY_BLUE, screen, screen_width // 2, 300 + i * 50)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_choice = choices[0]
                    elif event.key == pygame.K_2:
                        selected_choice = choices[1]
                    elif event.key == pygame.K_3:
                        selected_choice = choices[2]
                    elif event.key == pygame.K_4:
                        selected_choice = choices[3]

            if selected_choice is not None:
                if selected_choice == correct_answer:
                    screen.fill(BLACK)
                    draw_text("Correct!", font_large, COTTON_CANDY, screen, screen_width // 2, 300)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    break
                else:
                    screen.fill(BLACK)
                    draw_text("Wrong! Try again.", font_large, WRONG_COLOR, screen, screen_width // 2, 300)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    selected_choice = None

        return MAIN_MENU

def main():
    state = MAIN_MENU

    while True:
        if state == MAIN_MENU:
            state = main_menu()
        elif state == MATH_QUIZ:
            math_quiz(screen)
            state = MAIN_MENU
        elif state == MATH_MEMORY:
            math_memory(screen)
            state = MAIN_MENU
        elif state == ARITHMETIC_SEQUENCE:
            state = arithmetic_sequence(screen)

if __name__ == "__main__":
    main()