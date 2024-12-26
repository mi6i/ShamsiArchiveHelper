import sys
import inquirer
from src.folder_creator import create_date_with_subfolders
from src.compress import compress_to_zip_with_progress, compress_to_tar_with_progress
from src.utils import select_folder_tui, ask_to_delete_folder

def main_menu():
    """Display main menu and handle user input."""
    print("\n===== Main Menu =====")
    today_date = jdatetime.date.today().strftime("%Y-%m-%d")
    print(f"📅 Today's Jalali Date: {today_date}")

    while True:
        print("\n1. Create Today's Folder with Subfolders")
        print("2. Select Folder and Compress")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_date_with_subfolders()

        elif choice == "2":
            folder_to_compress = select_folder_tui()  # Folder selection TUI
            if folder_to_compress:
                print("\n🔧 Choose compression format:")
                print("1. ZIP (Standard)")
                print("2. TAR.GZ (Compressed)")

                format_choice = input("Enter your choice: ")

                if format_choice == "1":
                    archive_name = compress_to_zip_with_progress(folder_to_compress)
                elif format_choice == "2":
                    archive_name = compress_to_tar_with_progress(folder_to_compress)
                else:
                    print("❌ Invalid choice!")
                    continue

                if archive_name:
                    ask_to_delete_folder(folder_to_compress)  # Ask to delete folder after compression
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            sys.exit(0)
        else:
            print("❌ Invalid choice! Please try again.")
