import pygame
import subprocess
import shutil
import os.path
import logging
from typing import Dict, Optional

# Import game modules
import starters
import shop
import dedigivolve
import digivolve
import market
import digimondata
import enskills
import monsters
import easyest
import easy
import normal
import hard
import harder
import hardest
import choas
import button

class RandomizerApp:
    VERSION = "3.4"
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 1080
    BG_COLOR = (202, 228, 241)
    
    def __init__(self):
        pygame.init()
        self.setup_logging()
        self.screen = self.setup_display()
        self.buttons = self.load_buttons()
        self.running = True
        
    def setup_logging(self):
        logging.basicConfig(
            filename='randomizer.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info(f"Starting Randomizer v{self.VERSION}")
        
    def setup_display(self) -> pygame.Surface:
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Digimon CSHM - Randomizer')
        return screen
        
    def load_image(self, name: str) -> Optional[pygame.Surface]:
        try:
            return pygame.image.load(f'{name}_btn.png').convert_alpha()
        except pygame.error as e:
            logging.error(f"Failed to load image {name}_btn.png: {e}")
            return None
            
    def load_buttons(self) -> Dict[str, Dict]:
        """Load and configure all buttons"""
        buttons = {
            'main': {},
            'done': {},
            'reset': {}
        }
        
        # Button configurations
        button_configs = [
            ('start', 100, 50),
            ('shop', 100, 150),
            ('de', 100, 250),
            ('digi', 100, 350),
            ('di', 100, 450),
            ('mar', 100, 550),
            ('enskill', 100, 650),
            ('easyest', 750, 150),
            ('easy', 750, 250),
            ('normal', 750, 350),
            ('hard', 750, 450),
            ('harder', 750, 550),
            ('hardest', 750, 650),
            ('choas', 850, 150),
            ('text', 450, 150),
            ('mon', 450, 250),
            ('en', 725, 50),
            ('re', 450, 650)
        ]
        
        # Load done image once
        done_img = self.load_image('done')
        
        for btn_name, x, y in button_configs:
            img = self.load_image(btn_name)
            if img:
                buttons['main'][btn_name] = button.Button(x, y, img, 1)
                if done_img:
                    buttons['done'][btn_name] = button.Button(x, y, done_img, 1)
                buttons['reset'][btn_name] = button.Button(x, y, img, 1)
                
        return buttons
        
    def handle_button_click(self, btn_name: str) -> None:
        """Handle button click events"""
        try:
            if btn_name == 'start':
                starters.starters_func()
            elif btn_name == 'shop':
                shop.shop_func()
            elif btn_name == 'de':
                dedigivolve.dedigivolve_func(False)
            elif btn_name == 'di':
                digivolve.digivolve_func()
            elif btn_name == 'mar':
                market.market_func()
            elif btn_name == 'digi':
                digimondata.digimondata_func()
            elif btn_name == 'enskill':
                enskills.enskills_func()
            elif btn_name == 'easyest':
                easyest.encounters_func()
            elif btn_name == 'easy':
                easy.encounters_func()
            elif btn_name == 'normal':
                normal.encounters_func()
            elif btn_name == 'hard':
                hard.encounters_func()
            elif btn_name == 'harder':
                harder.encounters_func()
            elif btn_name == 'hardest':
                hardest.encounters_func()
            elif btn_name == 'choas':
                choas.encounters_func()
            elif btn_name == 'mon':
                monsters.monsters_func()
            elif btn_name == 'text':
                self.handle_textures()
                
            # Mark button as done
            self.buttons['main'][btn_name] = self.buttons['done'][btn_name]
            logging.info(f"{btn_name.capitalize()} function completed")
            
        except Exception as e:
            logging.error(f"Error in {btn_name} function: {e}")
            
    def handle_textures(self) -> None:
        """Handle texture randomization"""
        try:
            subprocess.call([r'.\randtexture.bat'])
            dir_name = "./textures"
            output_filename = "Random Textures"
            if os.path.exists(dir_name):
                shutil.make_archive(output_filename, 'zip', dir_name)
                logging.info("Textures randomized and archived successfully")
            else:
                logging.error(f"Texture directory not found: {dir_name}")
        except Exception as e:
            logging.error(f"Error processing textures: {e}")
            
    def handle_reset(self) -> None:
        """Reset all buttons to their original state"""
        for btn_name in self.buttons['main']:
            self.buttons['main'][btn_name] = self.buttons['reset'][btn_name]
        logging.info("All buttons reset")
        
    def run(self) -> None:
        """Main game loop"""
        print(f"version {self.VERSION}")
        
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # Draw background
            self.screen.fill(self.BG_COLOR)
            
            # Draw and handle buttons
            for btn_name, btn in self.buttons['main'].items():
                if btn.draw(self.screen):
                    if btn_name == 're':
                        self.handle_reset()
                    else:
                        self.handle_button_click(btn_name)
                        
            # Update display
            pygame.display.flip()
            
        pygame.quit()
        logging.info("Application closed")

if __name__ == '__main__':
    app = RandomizerApp()
    app.run()
