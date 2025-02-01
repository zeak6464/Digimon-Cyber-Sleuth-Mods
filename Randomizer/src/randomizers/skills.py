"""Skills randomizer module"""
from pathlib import Path
import random
import pandas as pd
import logging
import sys
import os

# Add src directory to Python path
src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from src.randomizers.base import BaseRandomizer
from src.config import RandomizerConfig

class SkillsRandomizer(BaseRandomizer):
    def __init__(self, config: RandomizerConfig):
        # Create the full directory path
        mod_dir = config.paths.MOD_DIR / "encounterskills/modfiles/data/battle_ai.mbe"
        mod_dir.mkdir(parents=True, exist_ok=True)
        
        super().__init__(
            input_path=mod_dir / "Ai.csv",
            backup_path=config.paths.BACKUP_DIR / "encounterskills_backup.csv",
            mod_name="Random Encounter Skills"
        )
        self.config = config
        self.skills_path = config.paths.INFO_DIR / "skills.csv"

    def create_template_df(self) -> pd.DataFrame:
        """Create a template DataFrame if file doesn't exist"""
        columns = ['id']
        # Add columns for each move (1-10)
        for i in range(1, 11):
            move_prefix = f'move{i}'
            columns.extend([
                f'{move_prefix}_id',
                f'{move_prefix}_unk1',
                f'{move_prefix}_unk2',
                f'{move_prefix}_unk3',
                f'{move_prefix}_unk4'
            ])
        return pd.DataFrame(columns=columns)

    def randomize(self) -> None:
        """Randomize encounter skills"""
        try:
            # Create initial file if it doesn't exist
            if not self.input_path.exists():
                df = self.create_template_df()
                df['id'] = list(range(1, 1001))  # Create enough entries
                df.to_csv(self.input_path, index=False)
            
            self.create_backup()
            
            # Get skills data
            if not self.skills_path.exists():
                raise FileNotFoundError(f"Skills file not found: {self.skills_path}")
            
            # Read skills into a list for random sampling
            # Explicitly convert to integers when reading
            skills_df = pd.read_csv(self.skills_path)
            skill_ids = skills_df['ID'].astype(int).tolist()  # Use column name 'ID'
            
            # Read or create skills data
            df = pd.read_csv(self.input_path)
            
            # Ensure we have all columns in correct order
            df = df.reindex(columns=self.create_template_df().columns)
            
            # Initialize all columns with 0
            for col in df.columns:
                if col != 'id':
                    df[col] = 0
            
            # For each entry
            for idx in df.index:
                # For each move slot (1-10)
                for i in range(1, 11):
                    move_prefix = f'move{i}'
                    # Randomize skill ID
                    df.at[idx, f'{move_prefix}_id'] = int(random.choice(skill_ids))  # Ensure integer
            
            # Save changes
            df.to_csv(self.input_path, index=False)
            self.create_zip(self.input_path.parent.parent.parent.parent)
            logging.info("Skills randomization complete")
            
        except Exception as e:
            logging.error(f"Failed to randomize skills: {e}")
            raise 