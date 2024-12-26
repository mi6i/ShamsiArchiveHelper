import os
import shutil
import inquirer

def select_folder_tui(start_folder="."):
    """Select folder through a text-based user interface."""
    current_folder = start_folder

    while True:
        try:
            items = [".."] + [
                item for item in os.listdir(current_folder)
                if os.path.isdir(os.path.join(current_folder, item))
            ]

            questions = [
                inquirer.List(
                    "folder",
                    message=f"📁 Current Folder: {os.path.abspath(current_folder)}",
                    choices=items,
                )
            ]
            answer = inquirer.prompt(questions)

            if not answer:
                print("❌ No selection made. Returning to the main menu.")
                return None

            selected = answer["folder"]

            if selected == "..":
                current_folder = os.path.abspath(os.path.join(current_folder, ".."))
            else:
                current_folder = os.path.join(current_folder, selected)

            confirm = inquirer.confirm(
                f"Select '{os.path.abspath(current_folder)}' as the target folder?",
                default=True,
            )
            if confirm:
                print(f"\n✅ Folder selected: {os.path.abspath(current_folder)}")
                return current_folder

        except KeyboardInterrupt:
            print("\n❗ Operation cancelled.")
            return None

def ask_to_delete_folder(folder_path):
    """Ask user whether to delete folder after compression."""
    confirm_delete = input(f"\n🗑️ Do you want to delete '{folder_path}' after compression? (y/n): ").strip().lower()
    if confirm_delete == "y":
        delete_folder(folder_path)
    else:
        print("ℹ️ Folder was not deleted.")

def delete_folder(folder_path):
    """Delete a folder safely."""
    try:
        shutil.rmtree(folder_path)
        print(f"🗑️ Deleted folder: '{folder_path}'")
    except Exception as e:
        print(f"❌ Error deleting folder: {e}")
