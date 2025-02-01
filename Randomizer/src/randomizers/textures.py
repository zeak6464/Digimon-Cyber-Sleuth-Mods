"""Texture randomizer module"""
import random
from pathlib import Path
import shutil
import logging
from .base import BaseRandomizer
from ..config import RandomizerConfig

class TextureRandomizer(BaseRandomizer):
    def __init__(self, config: RandomizerConfig):
        # Set up paths
        self.source_dir = Path("textures")  # Source textures directory
        mod_dir = config.paths.MOD_DIR / "modfiles/textures"  # Correct mod structure
        
        super().__init__(
            input_path=mod_dir,
            backup_path=config.paths.BACKUP_DIR / "textures_backup",
            mod_name="Random Textures"
        )
        self.config = config

    def randomize(self) -> None:
        """Randomize texture file names"""
        try:
            # Verify source directory exists
            if not self.source_dir.exists():
                raise FileNotFoundError(f"Textures directory not found at: {self.source_dir}")

            # Get list of texture files from modfiles/images
            texture_files = list((self.source_dir / "modfiles/images").glob("*.img"))
            if not texture_files:
                raise ValueError(f"No .img files found in {self.source_dir}/modfiles/images")

            # Create mod directory structure
            mod_images_dir = self.input_path / "images"
            mod_images_dir.mkdir(parents=True, exist_ok=True)

            # Create list of randomized file pairs
            file_pairs = list(zip(texture_files, random.sample(texture_files, len(texture_files))))

            # Copy files with randomized names
            for original, randomized in file_pairs:
                shutil.copy2(original, mod_images_dir / randomized.name)

            # Create the mod zip with correct structure
            temp_dir = Path("temp_mod")
            temp_dir.mkdir(exist_ok=True)
            
            # Create modfiles directory and copy textures
            modfiles_dir = temp_dir / "modfiles"
            modfiles_dir.mkdir(exist_ok=True)
            shutil.copytree(self.input_path.parent, modfiles_dir, dirs_exist_ok=True)
            
            # Create metadata file
            self.create_metadata(temp_dir)
            
            # Create zip
            output_filename = self.mod_name.replace(" ", "_")
            shutil.make_archive(output_filename, 'zip', temp_dir)
            logging.info("Texture randomization complete")
            
            # Clean up
            shutil.rmtree(temp_dir)

        except Exception as e:
            logging.error(f"Failed to randomize textures: {e}")
            if Path("temp_mod").exists():
                shutil.rmtree(Path("temp_mod"))
            raise 