"""Starters randomizer module"""
from pathlib import Path
import random
import pandas as pd
import logging
from .base import BaseRandomizer
from ..config import RandomizerConfig

class StartersRandomizer(BaseRandomizer):
    def __init__(self, config: RandomizerConfig):
        # Create paths for both files
        self.add_path = config.paths.MOD_DIR / "starters/modfiles/data/join_digimon_para_add.mbe/party.csv"
        self.cs_path = config.paths.MOD_DIR / "starters/modfiles/data/join_digimon_para.mbe/party.csv"
        
        super().__init__(
            input_path=self.add_path,
            backup_path=config.paths.BACKUP_DIR / "starters_backup.csv",
            mod_name="Random Starters"
        )
        self.config = config

    def create_template_df(self) -> pd.DataFrame:
        """Create a template DataFrame if file doesn't exist"""
        return pd.DataFrame(columns=[
            'id', 'digimon_id', 'unk1', 'unk2', 'unk3', 'unk4', 'unk5', 'unk6', 'unk7'
        ])

    def randomize(self) -> None:
        """Randomize starter Digimon"""
        try:
            # Create initial files if they don't exist
            for path in [self.add_path, self.cs_path]:
                if not path.exists():
                    path.parent.mkdir(parents=True, exist_ok=True)
                    self.create_template_df().to_csv(path, index=False)
            
            self.create_backup()
            
            # Get random Digimon sample
            digimon_df = pd.read_csv(self.config.paths.INFO_DIR / "digimon.csv").sample(n=8)
            
            # Process the starters data
            df = pd.read_csv(self.input_path)
            if df.empty:
                df = self.create_template_df()
                df['id'] = range(len(digimon_df))
            
            # Set Digimon IDs and default values
            df['digimon_id'] = digimon_df.index
            for col in ['unk1', 'unk2', 'unk3', 'unk4', 'unk5', 'unk6', 'unk7']:
                df[col] = 0
            
            # Save changes to both files
            for path in [self.add_path, self.cs_path]:
                df.to_csv(path, index=False)
            
            self.create_zip(self.input_path.parent.parent.parent.parent)
            logging.info("Starters randomization complete")
            
        except Exception as e:
            logging.error(f"Failed to randomize starters: {e}")
            raise 