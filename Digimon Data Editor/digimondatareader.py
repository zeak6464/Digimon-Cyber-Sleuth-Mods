import csv
import os
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class DigimonDataReader:
    def __init__(self):
        self.root = Tk()
        self.root.title('Digimon Data Reader')
        self.root.geometry('800x800')
        
        # Default paths
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.default_csv_path = os.path.join(self.base_dir, "digimondata", "modfiles", "data", "digimon_farm_para.mbe", "digimon.csv")
        self.images_dir = os.path.join(self.base_dir, "images")
        self.id_file_path = os.path.join(self.base_dir, "text files", "ID Alphabetized.txt")
        self.support_skills_path = os.path.join(self.base_dir, "text files", "Support Skills.txt")
        self.skills_path = os.path.join(self.base_dir, "text files", "Skills.txt")
        
        self.data = []
        self.current_image = None
        self.digimon_names = {}
        self.support_skills = {}
        self.skills = {}
        
        self.load_digimon_names()
        self.load_support_skills()
        self.load_skills()
        self.setup_ui()
        self.load_data()
        
    def load_skills(self):
        try:
            with open(self.skills_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if ':' in line:
                        id_str, skill = line.strip().split(':', 1)
                        self.skills[id_str] = skill
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load Skills: {str(e)}")
            
    def load_digimon_names(self):
        try:
            with open(self.id_file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if ':' in line:
                        id_str, name = line.strip().split(':', 1)
                        # Store both padded and unpadded versions of the ID
                        self.digimon_names[id_str] = name
                        # Convert to int and back to remove leading zeros
                        try:
                            num_id = int(id_str)
                            self.digimon_names[str(num_id)] = name
                        except ValueError:
                            pass
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load Digimon names: {str(e)}")
            
    def load_support_skills(self):
        try:
            with open(self.support_skills_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if ':' in line:
                        id_str, skill = line.strip().split(':', 1)
                        self.support_skills[id_str] = skill
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load Support Skills: {str(e)}")
            
    def get_padded_id(self, id_str):
        try:
            num_id = int(id_str)
            if num_id < 100:
                return f"{num_id:03d}"  # Pad with zeros to 3 digits
            return id_str
        except ValueError:
            return id_str
            
    def setup_ui(self):
        # Create main frames
        self.left_frame = ttk.Frame(self.root)
        self.left_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)
        
        self.right_frame = ttk.Frame(self.root)
        self.right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        
        # File selection button
        self.file_button = ttk.Button(self.left_frame, text="Open CSV File", command=self.select_file)
        self.file_button.pack(fill=X, pady=(0, 10))
        
        # Listbox with scrollbar
        self.listbox_frame = ttk.Frame(self.left_frame)
        self.listbox_frame.pack(fill=BOTH, expand=True)
        
        self.scrollbar = ttk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.listbox = Listbox(self.listbox_frame, yscrollcommand=self.scrollbar.set, height=15)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Bind listbox selection
        self.listbox.bind('<<ListboxSelect>>', lambda e: self.update())
        
        # Name label above image
        self.name_label = ttk.Label(self.right_frame, text="", font=('Arial', 14, 'bold'))
        self.name_label.pack(pady=(0, 5))
        
        # Image canvas
        self.canvas = Canvas(self.right_frame, width=300, height=300)
        self.canvas.pack(pady=(0, 10))
        
        # Create scrollable frame for stats
        self.canvas_frame = ttk.Frame(self.right_frame)
        self.canvas_frame.pack(fill=BOTH, expand=True)
        
        self.stats_canvas = Canvas(self.canvas_frame)
        self.scrollbar_stats = ttk.Scrollbar(self.canvas_frame, orient=VERTICAL, command=self.stats_canvas.yview)
        self.scrollable_frame = ttk.Frame(self.stats_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.stats_canvas.configure(scrollregion=self.stats_canvas.bbox("all"))
        )
        
        self.stats_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.stats_canvas.configure(yscrollcommand=self.scrollbar_stats.set)
        
        self.stats_canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar_stats.pack(side=RIGHT, fill=Y)
        
        # Create all labels
        self.create_stat_labels()
        
    def create_stat_labels(self):
        self.labels = {}
        stats = [
            "Id", "memoryUse", "growthType", "unknown", "baseHP", "baseSP",
            "baseATK", "baseDEF", "baseINT", "baseSPD", "maxLevel",
            "equipSlots", "supportSkill", "sMove1", "sMove1Level", "sMove2",
            "sMove2Level", "move1", "move1Level", "move2", "move2Level",
            "move3", "move3Level", "move4", "move4Level", "move5",
            "move5Level", "move6", "move6Level", "expValue", "levelCurve",
            "profile", "unknown2"
        ]
        
        for i, stat in enumerate(stats):
            frame = ttk.Frame(self.scrollable_frame)
            frame.pack(fill=X, padx=5, pady=2)
            
            label = ttk.Label(frame, text=stat)
            label.pack(side=LEFT, padx=(0, 10))
            
            value = ttk.Label(frame, text="")
            value.pack(side=LEFT)
            
            self.labels[stat] = value
            
    def select_file(self):
        filepath = filedialog.askopenfilename(
            initialdir=os.path.dirname(self.default_csv_path),
            title="Select CSV file",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        if filepath:
            self.default_csv_path = filepath
            self.load_data()
            
    def load_data(self):
        try:
            with open(self.default_csv_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.data = list(reader)
                # Remove header
                header = self.data.pop(0)
                
                # Update listbox
                self.listbox.delete(0, END)
                for row in self.data:
                    self.listbox.insert(END, row[0])
                    
                # Select first item
                if self.data:
                    self.listbox.selection_set(0)
                    self.update()
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file: {str(e)}")
            
    def load_image(self, digimon_id):
        try:
            # Try both padded and unpadded image paths
            padded_id = self.get_padded_id(digimon_id)
            image_path = os.path.join(self.images_dir, f"{padded_id}.png")
            if not os.path.exists(image_path):
                image_path = os.path.join(self.images_dir, f"{digimon_id}.png")
            if not os.path.exists(image_path):
                image_path = os.path.join(self.images_dir, "0.png")
                
            image = Image.open(image_path)
            # Resize image to fit canvas while maintaining aspect ratio
            image.thumbnail((300, 300))
            self.current_image = ImageTk.PhotoImage(image)
            self.canvas.delete("all")
            self.canvas.create_image(150, 150, image=self.current_image, anchor=CENTER)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
            
    def update(self):
        if not self.listbox.curselection():
            return
            
        try:
            index = self.listbox.curselection()[0]
            row = self.data[index]
            digimon_id = row[0]
            
            # Try both padded and unpadded versions of the ID
            padded_id = self.get_padded_id(digimon_id)
            digimon_name = self.digimon_names.get(padded_id, 
                          self.digimon_names.get(digimon_id, f"Unknown Digimon ({digimon_id})"))
            
            # Update name label
            self.name_label.config(text=digimon_name)
            
            # Update image
            self.load_image(padded_id)
            
            # Update all labels
            move_fields = {
                "sMove1": True, "sMove2": True,
                "move1": True, "move2": True, "move3": True,
                "move4": True, "move5": True, "move6": True
            }
            
            for i, (stat, label) in enumerate(self.labels.items()):
                if i < len(row):
                    value = row[i]
                    # Special handling for support skill
                    if stat == "supportSkill":
                        try:
                            skill_id = str(int(value))  # Convert to int and back to string to remove leading zeros
                            value = self.support_skills.get(skill_id, f"Unknown Skill ({value})")
                        except (ValueError, TypeError):
                            value = f"Invalid Skill ID ({value})"
                    # Special handling for moves
                    elif stat in move_fields:
                        try:
                            move_id = str(int(value))  # Convert to int and back to string to remove leading zeros
                            value = self.skills.get(move_id, f"Unknown Move ({value})")
                        except (ValueError, TypeError):
                            if value == "0" or not value:
                                value = "(None)"
                            else:
                                value = f"Invalid Move ID ({value})"
                    label.config(text=value)
                else:
                    label.config(text="N/A")
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update display: {str(e)}")
            
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = DigimonDataReader()
    app.run()
