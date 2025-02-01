"""Shop randomizer module"""
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

class ShopRandomizer(BaseRandomizer):
    def __init__(self, config: RandomizerConfig):
        # Create the full directory path
        mod_dir = config.paths.MOD_DIR / "shop/modfiles/data/shop_para.mbe"
        mod_dir.mkdir(parents=True, exist_ok=True)
        
        super().__init__(
            input_path=mod_dir / "lineup.csv",
            backup_path=config.paths.BACKUP_DIR / "shop_backup.csv",
            mod_name="Random Shop"
        )
        self.config = config
        self.items_path = config.paths.INFO_DIR / "item.csv"

    def create_template_df(self) -> pd.DataFrame:
        """Create a template DataFrame if file doesn't exist"""
        # Create columns: id + 100 item slots
        columns = ['id'] + [f'item{i}' for i in range(1, 101)]
        return pd.DataFrame(columns=columns)

    def randomize(self) -> None:
        """Randomize shop contents"""
        try:
            # Create initial file if it doesn't exist
            if not self.input_path.exists():
                df = self.create_template_df()
                df['id'] = list(range(1, 85))  # Number of shops from backup
                df.to_csv(self.input_path, index=False)
            
            self.create_backup()
            
            # Get items data
            if not self.items_path.exists():
                raise FileNotFoundError(f"Items file not found: {self.items_path}")
            
            # Read item IDs into a list for random sampling
            item_ids = pd.read_csv(self.items_path, header=None)[0].tolist()
            
            # Read or create shop data
            df = pd.read_csv(self.input_path)
            
            # Ensure we have all columns in correct order
            columns = ['id'] + [f'item{i}' for i in range(1, 101)]
            df = df.reindex(columns=columns)
            
            # For each shop entry
            for idx in df.index:
                # Randomly decide how many items (1-20)
                num_items = random.randint(1, 20)
                # Fill with random items
                items = random.choices(item_ids, k=num_items)
                # Fill the rest with zeros
                items.extend([0] * (100 - num_items))
                # Assign to item columns
                for i, item in enumerate(items, 1):
                    df.at[idx, f'item{i}'] = item
            
            # Ensure all columns are integers
            for col in df.columns:
                df[col] = df[col].fillna(0).astype(int)
            
            # Save changes
            df.to_csv(self.input_path, index=False)
            self.create_zip(self.input_path.parent.parent.parent.parent)
            logging.info("Shop randomization complete")
            
        except Exception as e:
            logging.error(f"Failed to randomize shop: {e}")
            raise 