"""Main Randomizer application"""
import tkinter as tk
from tkinter import ttk, messagebox
import logging
import threading
from pathlib import Path
from typing import Dict, Callable

from src.config import RandomizerConfig
from src.randomizers.shop import ShopRandomizer
from src.randomizers.encounters import EncountersRandomizer, DifficultyLevel
from src.randomizers.monsters import MonstersRandomizer
from src.randomizers.market import MarketRandomizer
from src.randomizers.digivolution import DigivolutionRandomizer
from src.randomizers.textures import TextureRandomizer
from src.randomizers.skills import SkillsRandomizer
from src.randomizers.starters import StartersRandomizer

class RandomizerApp:
    VERSION = "4.0"
    
    def __init__(self):
        self.config = RandomizerConfig()
        self.setup_logging()
        self.setup_window()
        self.create_widgets()
        
    def setup_logging(self):
        """Configure logging settings"""
        logging.basicConfig(
            filename='randomizer.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info(f"Starting Randomizer v{self.VERSION}")

    def setup_window(self):
        """Initialize the main window"""
        self.root = tk.Tk()
        self.root.title(f'Digimon CSHM - Randomizer v{self.VERSION}')
        self.root.geometry('800x600')
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('Action.TButton', padding=10)
        self.style.configure('Complete.TButton', 
                           background='green',
                           padding=10)
        
        # Create main frames
        self.create_frames()

    def create_frames(self):
        """Create the main layout frames"""
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Create columns for better organization
        self.left_frame = ttk.LabelFrame(self.main_frame, text="Main Actions", padding="5")
        self.left_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.middle_frame = ttk.LabelFrame(self.main_frame, text="Game Data", padding="5")
        self.middle_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        self.right_frame = ttk.LabelFrame(self.main_frame, text="Difficulty Settings", padding="5")
        self.right_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

    def create_widgets(self):
        """Create all buttons and widgets"""
        # Define button configurations
        self.button_configs = {
            'left': [
                ('Randomize Starters', lambda: StartersRandomizer(self.config).randomize()),
                ('Randomize Shop', lambda: ShopRandomizer(self.config).randomize()),
                ('Randomize De-Digivolution', lambda: DigivolutionRandomizer(self.config, True).randomize()),
                ('Randomize Digivolution', lambda: DigivolutionRandomizer(self.config).randomize()),
                ('Randomize Market', lambda: MarketRandomizer(self.config).randomize()),
            ],
            'middle': [
                ('Randomize Skills', lambda: SkillsRandomizer(self.config).randomize()),
                ('Randomize Monsters', lambda: MonstersRandomizer(self.config).randomize()),
                ('Randomize Textures', lambda: TextureRandomizer(self.config).randomize()),
            ],
            'right': [
                ('Easiest Encounters', lambda: EncountersRandomizer(self.config, DifficultyLevel.EASIEST).randomize()),
                ('Easy Encounters', lambda: EncountersRandomizer(self.config, DifficultyLevel.EASY).randomize()),
                ('Normal Encounters', lambda: EncountersRandomizer(self.config, DifficultyLevel.NORMAL).randomize()),
                ('Hard Encounters', lambda: EncountersRandomizer(self.config, DifficultyLevel.HARD).randomize()),
                ('Harder Encounters', lambda: EncountersRandomizer(self.config, DifficultyLevel.HARDER).randomize()),
                ('Hardest Encounters', lambda: EncountersRandomizer(self.config, DifficultyLevel.HARDEST).randomize()),
                ('Chaos Encounters', lambda: EncountersRandomizer(self.config, DifficultyLevel.CHAOS).randomize()),
            ]
        }
        
        # Create buttons
        self.buttons: Dict[str, ttk.Button] = {}
        
        for i, (text, command) in enumerate(self.button_configs['left']):
            self.create_button(self.left_frame, text, command, i)
            
        for i, (text, command) in enumerate(self.button_configs['middle']):
            self.create_button(self.middle_frame, text, command, i)
            
        for i, (text, command) in enumerate(self.button_configs['right']):
            self.create_button(self.right_frame, text, command, i)
            
        # Add reset button at the bottom
        self.reset_button = ttk.Button(
            self.main_frame,
            text="Reset All",
            command=self.handle_reset,
            style='Action.TButton'
        )
        self.reset_button.grid(row=1, column=0, columnspan=3, pady=10)

    def create_button(self, parent: ttk.Frame, text: str, command: Callable, row: int):
        """Helper method to create a button with consistent styling"""
        btn = ttk.Button(
            parent,
            text=text,
            command=lambda cmd=command, txt=text: self.handle_button_click(cmd, txt),
            style='Action.TButton'
        )
        btn.grid(row=row, column=0, padx=5, pady=2, sticky="ew")
        self.buttons[text] = btn

    def handle_button_click(self, command: Callable, button_text: str):
        """Handle button clicks with error handling and threading"""
        def run_command():
            try:
                command()
                self.root.after(0, self.mark_complete, button_text)
                logging.info(f"{button_text} completed successfully")
            except Exception as e:
                self.root.after(0, self.show_error, button_text, str(e))
                logging.error(f"Error in {button_text}: {e}")

        # Run the command in a separate thread
        thread = threading.Thread(target=run_command)
        thread.daemon = True
        thread.start()

    def mark_complete(self, button_text: str):
        """Mark a button as complete"""
        btn = self.buttons[button_text]
        btn.configure(style='Complete.TButton')
        btn.state(['disabled'])

    def handle_reset(self):
        """Reset all buttons to their original state"""
        for btn in self.buttons.values():
            btn.configure(style='Action.TButton')
            btn.state(['!disabled'])
        logging.info("All buttons reset")

    def show_error(self, action: str, error_msg: str):
        """Show error message to user"""
        messagebox.showerror(
            "Error",
            f"Error during {action}:\n{error_msg}"
        )

    def run(self):
        """Start the application"""
        print(f"Version {self.VERSION}")
        self.root.mainloop()

if __name__ == '__main__':
    app = RandomizerApp()
    app.run()
