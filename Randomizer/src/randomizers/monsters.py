"""Monsters randomizer module"""
from pathlib import Path
import random
import pandas as pd
import logging
from .base import BaseRandomizer
from ..config import RandomizerConfig

class MonstersRandomizer(BaseRandomizer):
    def __init__(self, config: RandomizerConfig):
        # Create the full directory path
        mod_dir = config.paths.MOD_DIR / "monsters/modfiles/data/mon_para.mbe"
        mod_dir.mkdir(parents=True, exist_ok=True)
        
        super().__init__(
            input_path=mod_dir / "Monster.csv",
            backup_path=config.paths.BACKUP_DIR / "mon_para_backup.csv",
            mod_name="Random Monster Easy"
        )
        self.config = config

    def create_template_df(self) -> pd.DataFrame:
        """Create a template DataFrame if file doesn't exist"""
        return pd.DataFrame(columns=[
            'id', 'EXP', 'EXPx2', 'YEN', 'YENx2', 
            'itemChance1', 'itemChance2', 'scanRate',
            'unk1', 'unk2', 'unk3', 'unk4'
        ])

    def randomize(self) -> None:
        """Randomize monster parameters"""
        try:
            # Create initial file if it doesn't exist
            if not self.input_path.exists():
                self.create_template_df().to_csv(self.input_path, index=False)
            
            self.create_backup()
            
            # Read or create monster data
            df = pd.read_csv(self.input_path)
            if df.empty:
                df = self.create_template_df()
                df['id'] = range(1000)  # Create entries for all possible monsters
            
            # Modify monster parameters
            df['EXP'] = df['EXP'].apply(lambda x: x + 1000 if pd.notnull(x) else 1000)
            df['EXPx2'] = df['EXPx2'].apply(lambda x: x + 10000 if pd.notnull(x) else 10000)
            df['YEN'] = df['YEN'].apply(lambda x: x + 1000 if pd.notnull(x) else 1000)
            df['YENx2'] = df['YENx2'].apply(lambda x: x + 10000 if pd.notnull(x) else 10000)
            df['itemChance1'] = 100
            df['itemChance2'] = 100
            df['scanRate'] = 100
            
            # Set default values for unknown columns
            for col in ['unk1', 'unk2', 'unk3', 'unk4']:
                df[col] = 0
            
            # Save changes
            df.to_csv(self.input_path, index=False)
            self.create_zip(self.input_path.parent.parent.parent.parent)
            logging.info("Monster randomization complete")
            
        except Exception as e:
            logging.error(f"Failed to randomize monsters: {e}")
            raise 