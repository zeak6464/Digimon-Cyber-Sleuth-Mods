"""Digivolution randomizer module"""
from pathlib import Path
import random
import pandas as pd
import logging
from .base import BaseRandomizer
from ..config import RandomizerConfig

class DigivolutionRandomizer(BaseRandomizer):
    def __init__(self, config: RandomizerConfig, is_dedigivolution: bool = False):
        # Set up paths based on type
        self.is_dedigivolution = is_dedigivolution
        mod_name = "Random DeDigivolve" if is_dedigivolution else "Random Digivolve"
        mod_path = "dedigivolve" if is_dedigivolution else "digivolve"
        file_name = "degeneration_para.mbe" if is_dedigivolution else "evolution_next_para.mbe"
        
        # Create the full directory path
        mod_dir = config.paths.MOD_DIR / f"{mod_path}/modfiles/data/{file_name}"
        mod_dir.mkdir(parents=True, exist_ok=True)
        
        super().__init__(
            input_path=mod_dir / "digimon.csv",
            backup_path=config.paths.BACKUP_DIR / f"{mod_path}_backup.csv",
            mod_name=mod_name
        )
        self.config = config
        self.stages = config.stages

    def create_template_df(self) -> pd.DataFrame:
        """Create a template DataFrame if file doesn't exist"""
        return pd.DataFrame(columns=[
            'id', 'digi1', 'digi2', 'digi3', 'digi4', 'digi5', 'digi6'
        ])

    def get_stage(self, digimon_id: int) -> int:
        """Get the evolution stage of a Digimon by its ID"""
        stage_lists = [
            (self.stages.BABY, 0),
            (self.stages.BABY_TWO, 1),
            (self.stages.CHILD, 2),
            (self.stages.ADULT, 3),
            (self.stages.PERFECT, 4),
            (self.stages.ULTIMATE, 5),
            (self.stages.ULTIMATE_PLUS, 6)
        ]
        
        for stage_list, stage_num in stage_lists:
            if digimon_id in stage_list:
                return stage_num
        return -1

    def get_potential_evolutions(self, stage: int) -> list:
        """Get list of potential evolutions for a stage"""
        if self.is_dedigivolution and stage == 0:
            return []
        if not self.is_dedigivolution and stage == 6:
            return []
            
        next_stage = stage - 1 if self.is_dedigivolution else stage + 1
        stage_map = {
            0: self.stages.BABY,
            1: self.stages.BABY_TWO,
            2: self.stages.CHILD,
            3: self.stages.ADULT,
            4: self.stages.PERFECT,
            5: self.stages.ULTIMATE,
            6: self.stages.ULTIMATE_PLUS
        }
        return stage_map.get(next_stage, [])

    def randomize(self) -> None:
        """Randomize digivolution paths"""
        try:
            # Create initial file if it doesn't exist
            if not self.input_path.exists():
                self.create_template_df().to_csv(self.input_path, index=False)
            
            self.create_backup()
            
            # Read or create digivolution data
            df = pd.read_csv(self.input_path)
            if df.empty:
                df = self.create_template_df()
                df['id'] = range(300)  # Create 300 digivolution entries
            
            # Process each row
            for i, row in df.iterrows():
                # Initialize with -1 for all digi slots
                for j in range(1, 7):
                    df.at[i, f'digi{j}'] = -1
                
                # Get stage and potential evolutions
                mon_stage = self.get_stage(row['id'])
                if mon_stage not in [-1, 0 if self.is_dedigivolution else 6]:
                    potential_evos = self.get_potential_evolutions(mon_stage)
                    if potential_evos:
                        num_evos = random.randint(1, min(6, len(potential_evos)))
                        evolutions = random.sample(potential_evos, num_evos)
                        
                        # Assign evolutions to digi slots
                        for j, evo in enumerate(evolutions, 1):
                            df.at[i, f'digi{j}'] = evo
            
            # Save changes
            df.to_csv(self.input_path, index=False)
            self.create_zip(self.input_path.parent.parent.parent.parent)
            logging.info(f"{'De-digivolution' if self.is_dedigivolution else 'Digivolution'} randomization complete")
            
        except Exception as e:
            logging.error(f"Failed to randomize {'de-digivolution' if self.is_dedigivolution else 'digivolution'}: {e}")
            raise 