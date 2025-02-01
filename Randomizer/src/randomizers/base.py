"""Base randomizer module"""
from pathlib import Path
import logging
import shutil
import json
from typing import Optional
import pandas as pd
import sys
import os

# Add src directory to Python path
src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from src.config import RandomizerConfig

class BaseRandomizer:
    def __init__(self, input_path: Path, backup_path: Path, mod_name: str):
        self.input_path = input_path
        self.backup_path = backup_path
        self.mod_name = mod_name
        
        # Create mod directories if they don't exist
        self.input_path.parent.mkdir(parents=True, exist_ok=True)
        self.setup_logging()
        
    def setup_logging(self):
        """Configure logging for the randomizer"""
        logging.basicConfig(
            filename='randomizer.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
    def create_backup(self) -> None:
        """Create a backup of the input file if it doesn't exist"""
        if not self.backup_path.exists() and self.input_path.exists():
            self.backup_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.input_path, self.backup_path)
            logging.info(f"Created backup at {self.backup_path}")
            
    def create_metadata(self, temp_dir: Path) -> None:
        """Create METADATA.json file for the mod"""
        metadata = {
            "name": self.mod_name,
            "description": f"Randomized {self.mod_name} mod",
            "version": "1.0",
            "author": "Randomizer",
            "category": "Gameplay"
        }
        
        metadata_path = temp_dir / "METADATA.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=4)
        logging.info(f"Created metadata file at {metadata_path}")

    def create_zip(self, base_dir: Path) -> None:
        """Create a zip file of the mod with metadata"""
        try:
            output_filename = self.mod_name.replace(" ", "_")
            temp_dir = Path("temp_mod")
            
            # Create temporary directory for mod files
            temp_dir.mkdir(exist_ok=True)
            
            # Copy mod files to temp directory maintaining correct structure
            if base_dir.exists():
                # Create modfiles directory at root level
                modfiles_dir = temp_dir / "modfiles"
                modfiles_dir.mkdir(exist_ok=True)
                
                # Copy contents of base_dir to modfiles directory
                # This ensures modfiles is at the root level next to METADATA.json
                for item in base_dir.iterdir():
                    if item.is_dir():
                        shutil.copytree(item, modfiles_dir / item.name, dirs_exist_ok=True)
                    else:
                        shutil.copy2(item, modfiles_dir / item.name)
                
                # Create metadata file at root level
                self.create_metadata(temp_dir)
                
                # Create zip from temp directory
                shutil.make_archive(output_filename, 'zip', temp_dir)
                logging.info(f"Created zip file: {output_filename}.zip")
                
                # Clean up temp directory
                shutil.rmtree(temp_dir)
            else:
                raise FileNotFoundError(f"Base directory not found: {base_dir}")
                
        except Exception as e:
            logging.error(f"Failed to create zip file: {e}")
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
            raise
            
    def randomize(self) -> None:
        """Base randomize method to be implemented by subclasses"""
        raise NotImplementedError 