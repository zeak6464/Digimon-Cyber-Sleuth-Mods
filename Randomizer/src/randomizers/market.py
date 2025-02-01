"""Market randomizer module"""
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

class MarketRandomizer(BaseRandomizer):
    def __init__(self, config: RandomizerConfig):
        # Create the full directory path
        mod_dir = config.paths.MOD_DIR / "market/modfiles/data/digimon_market_para.mbe"
        mod_dir.mkdir(parents=True, exist_ok=True)
        
        super().__init__(
            input_path=mod_dir / "table.csv",
            backup_path=config.paths.BACKUP_DIR / "market_backup.csv",
            mod_name="Random DigiMarket"
        )
        self.config = config
        self.digimon_path = config.paths.INFO_DIR / "digimon.csv"

    def create_template_df(self) -> pd.DataFrame:
        """Create a template DataFrame if file doesn't exist"""
        # Exact column order from backup
        columns = ['id', 'digimonId', 'unknown1', 'price', 'level', 'unknown3']
        return pd.DataFrame(columns=columns)

    def randomize(self) -> None:
        """Randomize market contents"""
        try:
            # Create initial file if it doesn't exist
            if not self.input_path.exists():
                df = self.create_template_df()
                df['id'] = list(range(1, 51))  # Convert range to list
                df.to_csv(self.input_path, index=False)
            
            self.create_backup()
            
            # Get Digimon data
            if not self.digimon_path.exists():
                raise FileNotFoundError(f"Digimon file not found: {self.digimon_path}")
            
            # Read Digimon IDs into a list for random sampling
            digimon_ids = pd.read_csv(self.digimon_path, header=None)[0].tolist()
            
            # Read or create market data
            df = pd.read_csv(self.input_path)
            
            # Ensure we have the correct columns in the correct order
            df = df.reindex(columns=['id', 'digimonId', 'unknown1', 'price', 'level', 'unknown3'])
            
            # Randomize values while maintaining structure
            num_entries = len(df)
            df['digimonId'] = random.choices(digimon_ids, k=num_entries)
            df['unknown1'] = list(range(1, num_entries + 1))  # Convert range to list
            df['price'] = 2500
            df['level'] = 1
            df['unknown3'] = 3600
            
            # Ensure all columns are integers
            for col in df.columns:
                df[col] = df[col].astype(int)
            
            # Save changes
            df.to_csv(self.input_path, index=False)
            self.create_zip(self.input_path.parent.parent.parent.parent)
            logging.info("Market randomization complete")
            
        except Exception as e:
            logging.error(f"Failed to randomize market: {e}")
            raise 