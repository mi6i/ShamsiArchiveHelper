import os
import jdatetime
import json
import logging

# Logging Configuration
logging.basicConfig(
    filename="logs/folder_compressor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def load_config():
    """Load folder names from config file."""
    try:
        with open("config/config.json", "r") as config_file:
            config = json.load(config_file)
            return config.get("subfolders", [])
    except FileNotFoundError:
        print("❌ Config file not found. Using default subfolders.")
        return [
            "KaraWeb", "Rahkaran", "Rahkaran Factory", 
            "Vision Factory", "Vision Maliati", "Vision Pakhsh"
        ]
    except json.JSONDecodeError:
        print("❌ Error parsing config file. Using default subfolders.")
        return [
            "KaraWeb", "Rahkaran", "Rahkaran Factory", 
            "Vision Factory", "Vision Maliati", "Vision Pakhsh"
        ]

def create_date_with_subfolders():
    """Create today's folder and subfolders based on the config."""
    today_date = jdatetime.date.today().strftime("%Y-%m-%d")
    main_folder = today_date

    subfolders = load_config()  # Load subfolders from config

    try:
        if not os.path.exists(main_folder):
            os.makedirs(main_folder)
            print(f"✅ Created main folder: '{main_folder}'")
        else:
            print(f"ℹ️ Main folder '{main_folder}' already exists.")

        for subfolder in subfolders:
            subfolder_path = os.path.join(main_folder, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
                print(f"  └── Created subfolder: '{subfolder_path}'")
            else:
                print(f"  └── Subfolder already exists: '{subfolder_path}'")

        print("\n✅ All folders and subfolders created successfully.")
    except Exception as e:
        print(f"❌ Error creating folders: {e}")
        logging.error(f"Error creating folders: {e}")
