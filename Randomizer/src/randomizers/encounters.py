"""Encounters randomizer module"""
from enum import Enum
from pathlib import Path
import random
import pandas as pd
import logging
from .base import BaseRandomizer
from ..config import RandomizerConfig

class DifficultyLevel(Enum):
    """Available difficulty levels for encounters"""
    EASIEST = 1
    EASY = 2
    NORMAL = 3
    HARD = 4
    HARDER = 5
    HARDEST = 6
    CHAOS = 7

    @property
    def num_encounters(self) -> int:
        """Number of encounters for this difficulty"""
        return {
            DifficultyLevel.EASIEST: 1,
            DifficultyLevel.EASY: 2,
            DifficultyLevel.NORMAL: 3,
            DifficultyLevel.HARD: 4,
            DifficultyLevel.HARDER: 5,
            DifficultyLevel.HARDEST: 3,
            DifficultyLevel.CHAOS: 6,
        }[self]

class EncountersRandomizer(BaseRandomizer):
    def __init__(self, config: RandomizerConfig, difficulty: DifficultyLevel):
        # Create the full directory path for encounters
        mod_dir = config.paths.MOD_DIR / "encounters/modfiles/data/mon_cpl.mbe"
        mod_dir.mkdir(parents=True, exist_ok=True)  # Create directories if they don't exist
        
        super().__init__(
            input_path=mod_dir / "Coupling.csv",
            backup_path=config.paths.BACKUP_DIR / "encounters_backup.csv",
            mod_name=f"Random Encounters {difficulty.name}"
        )
        self.config = config
        self.difficulty = difficulty
        self.stages = config.stages
        
    def get_stage(self, digimon_id: int) -> int:
        """Get the evolution stage of a Digimon by its ID"""
        stage_lists = [
            (self.stages.BABY, 0),
            (self.stages.BABY_TWO, 1),
            (self.stages.CHILD, 2),
            (self.stages.ADULT, 3),
            (self.stages.PERFECT, 4),
            (self.stages.ULTIMATE, 5),
            (self.stages.ULTIMATE_PLUS, 6),
            (self.stages.EATERS, 7),
            (self.stages.GATES, 8)
        ]
        
        for stage_list, stage_num in stage_lists:
            if digimon_id in stage_list:
                return stage_num
        return -1

    def get_potential_encounters(self, stage: int) -> list:
        """Get list of potential encounters for a stage"""
        stage_map = {
            0: self.stages.BABY,
            1: self.stages.BABY_TWO,
            2: self.stages.CHILD,
            3: self.stages.ADULT,
            4: self.stages.PERFECT,
            5: self.stages.ULTIMATE,
            6: self.stages.ULTIMATE_PLUS,
            7: self.stages.EATERS,
            8: self.stages.GATES
        }
        return stage_map.get(stage, [])

    def randomize(self) -> None:
        """Randomize encounters based on difficulty level"""
        try:
            # Create initial Coupling.csv if it doesn't exist
            if not self.input_path.exists():
                # Create a basic template file
                df = pd.DataFrame(columns=[
                    'id', 'digi1', 'digi2', 'digi3', 'digi4', 'digi5', 'digi6',
                    'level1', 'level2', 'level3', 'level4', 'level5', 'level6',
                    'variation1', 'variation2', 'variation3', 'variation4', 'variation5', 'variation6',
                    'unk13', 'unk14', 'unk15', 'unk16', 'unk9', 'unk10'
                ])
                df.to_csv(self.input_path, index=False)
            
            # Rest of the randomization code...
            self.create_backup()
            original_df = pd.read_csv(self.input_path)
            
            # Create new DataFrame with same structure
            df = pd.DataFrame(columns=original_df.columns)
            df['id'] = original_df['id'] if not original_df.empty else range(1000)  # Use range if empty
            
            # Process each row
            for i, row in df.iterrows():
                # Initialize with -1 for all digi slots
                for j in range(1, 7):
                    df.at[i, f'digi{j}'] = -1
                
                # Get stage and potential encounters
                mon_stage = self.get_stage(original_df.at[i, 'digi1']) if not original_df.empty else 3  # Default to Adult
                if mon_stage not in [-1, 0, 7, 8, 9]:
                    potential_evos = self.get_potential_encounters(mon_stage)
                    if potential_evos:
                        num_encounters = min(self.difficulty.num_encounters, len(potential_evos))
                        evolutions = random.sample(potential_evos, num_encounters)
                        
                        # Assign evolutions to digi slots
                        for j, evo in enumerate(evolutions, 1):
                            df.at[i, f'digi{j}'] = evo
                
                # Set default values
                for j in range(1, 7):
                    df.at[i, f'level{j}'] = original_df.at[i, f'level{j}'] if not original_df.empty else 50
                    df.at[i, f'variation{j}'] = 1
                
                # Set unknown values
                for j in range(13, 17):
                    df.at[i, f'unk{j}'] = 0
                df.at[i, 'unk9'] = 0
                df.at[i, 'unk10'] = 'a'
            
            # Save changes
            df.to_csv(self.input_path, index=False)
            self.create_zip(self.input_path.parent.parent.parent.parent)
            logging.info(f"Encounters randomization complete for {self.difficulty.name}")
            
        except Exception as e:
            logging.error(f"Failed to randomize encounters: {e}")
            raise 