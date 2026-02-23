import pygame
import random
import math

# Initialize Pygame
pygame.init()
pygame.font.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circuit Tester Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NEON_BLUE = (0, 255, 255)
NEON_GREEN = (0, 255, 0)
NEON_RED = (255, 0, 0)
GRAY = (100, 100, 100)
DARK_GREEN = (0, 50, 0)
GLOW_YELLOW = (255, 255, 100)

# Fonts
try:
    FONT = pygame.font.SysFont("orbitron", 24)  # Futuristic font
except:
    FONT = pygame.font.SysFont("arial", 24)

# Game variables
MAX_GUESSES = 10
VOLTAGE_RANGE = (1, 10)

class Particle:
    """Enhanced particle for feedback effects (sparks and glows)."""
    def __init__(self, x, y, color, is_spark=False):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3) if is_spark else random.uniform(-1, 1)
        self.vy = random.uniform(-3, 3) if is_spark else random.uniform(-1, 1)
        self.color = color
        self.lifetime = 40 if is_spark else 60
        self.is_spark = is_spark
        self.size = random.randint(2, 5) if is_spark else 4

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1
        if self.is_spark:
            self.size = max(1, self.size - 0.1)

    def draw(self, surface):
        if self.lifetime > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))

class CircuitTesterGame:
    def __init__(self):
        self.correct_voltage = random.randint(VOLTAGE_RANGE[0], VOLTAGE_RANGE[1])
        self.guess_list = []
        self.attempts = 0
        self.feedback = "Enter guess (1-10) and press Enter!"
        self.feedback_color = NEON_BLUE
        self.input_text = ""
        self.game_over = False
        self.particles = []
        self.cursor_visible = True
        self.cursor_timer = 0
        self.wave_phase = 0  # For oscilloscope animation
        
        # Detailed circuit board background
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill(DARK_GREEN)  # PCB green
        for _ in range(100):  # Dense circuit traces
            x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            x2, y2 = x1 + random.randint(-80, 80), y1 + random.randint(-80, 80)
            pygame.draw.line(self.background, GRAY, (x1, y1), (x2, y2), 1)
        for _ in range(20):  # Solder points
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            pygame.draw.circle(self.background, GLOW_YELLOW, (x, y), 3)

    def process_guess(self, guess_text):
        """Process the player's guess."""
        try:
            guess = int(guess_text)
            if guess < VOLTAGE_RANGE[0] or guess > VOLTAGE_RANGE[1]:
                self.feedback = "Error: Guess must be 1-10!"
                self.feedback_color = NEON_RED
                self.add_particles(300, 100, NEON_RED, is_spark=True)
                return
            
            self.guess_list.append(guess)
            self.attempts += 1
            
            if guess == self.correct_voltage:
                self.feedback = f"Correct! Voltage is {self.correct_voltage}!"
                self.feedback_color = NEON_GREEN
                self.add_particles(300, 100, NEON_GREEN, is_spark=False)
                self.game_over = True
            elif guess > self.correct_voltage:
                self.feedback = "Too high!"
                self.feedback_color = NEON_RED
                self.add_particles(300, 100, NEON_RED, is_spark=True)
            else:
                self.feedback = "Too low!"
                self.feedback_color = NEON_BLUE
                self.add_particles(300, 100, NEON_BLUE, is_spark=True)
                
            if self.attempts >= MAX_GUESSES and not self.game_over:
                self.feedback = f"Game Over! Voltage was {self.correct_voltage}."
                self.feedback_color = NEON_RED
                self.add_particles(300, 100, NEON_RED, is_spark=True)
                self.game_over = True
                
        except ValueError:
            self.feedback = "Error: Enter a valid integer!"
            self.feedback_color = NEON_RED
            self.add_particles(300, 100, NEON_RED, is_spark=True)

    def add_particles(self, x, y, color, is_spark=False):
        """Add enhanced particles (sparks or glows)."""
        for _ in range(30):  # More particles
            self.particles.append(Particle(x, y, color, is_spark))

    def reset_game(self):
        """Reset the game."""
        self.correct_voltage = random.randint(VOLTAGE_RANGE[0], VOLTAGE_RANGE[1])
        self.guess_list = []
        self.attempts = 0
        self.feedback = "Enter guess (1-10) and press Enter!"
        self.feedback_color = NEON_BLUE
        self.input_text = ""
        self.game_over = False
        self.particles = []
        self.wave_phase = 0

    def draw_voltmeter(self, surface, guess=None):
        """Draw 3D-like voltmeter with glowing needle."""
        center = (300, 300)
        radius = 100
        # 3D gauge (gradient effect)
        for r in range(radius, radius - 10, -1):
            shade = min(150 + (radius - r) * 10, 255)
            pygame.draw.circle(surface, (shade, shade, shade), center, r)
        pygame.draw.circle(surface, WHITE, center, radius - 5, 3)
        
        # Ticks with depth
        for i in range(1, 11):
            angle = math.radians(135 - (i * 27))
            x1 = center[0] + (radius - 15) * math.cos(angle)
            y1 = center[1] - (radius - 15) * math.sin(angle)
            x2 = center[0] + radius * math.cos(angle)
            y2 = center[1] - radius * math.sin(angle)
            pygame.draw.line(surface, WHITE, (x1, y1), (x2, y2), 3)
            # 3D tick labels
            label_x = center[0] + (radius + 25) * math.cos(angle)
            label_y = center[1] - (radius + 25) * math.sin(angle)
            label = FONT.render(str(i), True, NEON_BLUE)
            shadow = FONT.render(str(i), True, BLACK)
            surface.blit(shadow, (label_x - 12, label_y - 8))
            surface.blit(label, (label_x - 10, label_y - 10))
        
        # Glowing needle
        if guess is not None and 1 <= guess <= 10:
            angle = math.radians(135 - (guess * 27))
            x = center[0] + (radius - 20) * math.cos(angle)
            y = center[1] - (radius - 20) * math.sin(angle)
            pygame.draw.line(surface, NEON_RED, center, (x, y), 5)
            pygame.draw.circle(surface, GLOW_YELLOW, (int(x), int(y)), 8, 1)  # Glow effect

    def draw_oscilloscope(self, surface, guess=None):
        """Draw oscilloscope waveform based on guess."""
        pygame.draw.rect(surface, BLACK, (150, 50, 300, 80))  # Oscilloscope screen
        pygame.draw.rect(surface, WHITE, (150, 50, 300, 80), 2)
        if guess is not None and 1 <= guess <= 10:
            amplitude = guess * 5  # Scale amplitude
            for x in range(151, 449):
                t = (x - 151 + self.wave_phase) / 20
                y = 90 + amplitude * math.sin(t)
                pygame.draw.circle(surface, NEON_GREEN, (x, int(y)), 1)
        self.wave_phase += 0.1  # Animate wave

    def draw_capacitor(self, surface):
        """Draw animated capacitor (pulses when active)."""
        x, y = 500, 100
        pulse = 10 if not self.game_over else 0
        if not self.game_over:
            pulse += math.sin(self.wave_phase * 2) * 5
        # Capacitor plates
        pygame.draw.line(surface, GRAY, (x - 20, y), (x - 10, y), 4)
        pygame.draw.line(surface, GRAY, (x + 10, y), (x + 20, y), 4)
        # Glow effect
        pygame.draw.circle(surface, GLOW_YELLOW, (x, y), int(5 + pulse), 1)

    def run(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if not self.game_over:
                        if event.key == pygame.K_RETURN:
                            if self.input_text:
                                self.process_guess(self.input_text)
                                self.input_text = ""
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        elif event.unicode.isdigit() and len(self.input_text) < 2:
                            self.input_text += event.unicode
                    elif event.key == pygame.K_r:
                        self.reset_game()
            
            # Update cursor blink
            self.cursor_timer += 1
            if self.cursor_timer >= 30:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0
            
            # Draw background
            screen.blit(self.background, (0, 0))
            
            # Draw oscilloscope
            current_guess = int(self.input_text) if self.input_text.isdigit() else None
            self.draw_oscilloscope(screen, current_guess)
            
            # Draw voltmeter
            self.draw_voltmeter(screen, current_guess)
            
            # Draw capacitor
            self.draw_capacitor(screen)
            
            # Draw feedback with shadow
            feedback_text = FONT.render(self.feedback, True, self.feedback_color)
            shadow_text = FONT.render(self.feedback, True, BLACK)
            screen.blit(shadow_text, (302 - feedback_text.get_width() // 2, 152))
            screen.blit(feedback_text, (300 - feedback_text.get_width() // 2, 150))
            
            # Draw input box with cursor
            input_surface = FONT.render(self.input_text, True, WHITE)
            pygame.draw.rect(screen, GRAY, (250, 450, 100, 30))
            screen.blit(input_surface, (260, 455))
            if self.cursor_visible and not self.game_over:
                cursor_x = 260 + input_surface.get_width()
                pygame.draw.line(screen, WHITE, (cursor_x, 455), (cursor_x, 475), 2)
            
            # Draw attempts with shadow
            attempts_text = FONT.render(f"Attempts: {self.attempts}/{MAX_GUESSES}", True, WHITE)
            shadow_attempts = FONT.render(f"Attempts: {self.attempts}/{MAX_GUESSES}", True, BLACK)
            screen.blit(shadow_attempts, (302 - attempts_text.get_width() // 2, 502))
            screen.blit(attempts_text, (300 - attempts_text.get_width() // 2, 500))
            
            # Draw guess history with shadow
            history_text = FONT.render(f"Guesses: {self.guess_list}", True, WHITE)
            shadow_history = FONT.render(f"Guesses: {self.guess_list}", True, BLACK)
            screen.blit(shadow_history, (302 - history_text.get_width() // 2, 532))
            screen.blit(history_text, (300 - history_text.get_width() // 2, 530))
            
            # Draw particles
            for particle in self.particles[:]:
                particle.update()
                particle.draw(screen)
                if particle.lifetime <= 0:
                    self.particles.remove(particle)
            
            # Draw play again prompt
            if self.game_over:
                replay_text = FONT.render("Press R to Play Again", True, NEON_GREEN)
                shadow_replay = FONT.render("Press R to Play Again", True, BLACK)
                screen.blit(shadow_replay, (302 - replay_text.get_width() // 2, 562))
                screen.blit(replay_text, (300 - replay_text.get_width() // 2, 560))
            
            pygame.display.flip()
            clock.tick(60)

def main():
    """Run the Circuit Tester Game with Pygame."""
    game = CircuitTesterGame()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()