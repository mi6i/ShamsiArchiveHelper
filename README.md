# 🌟 Folder Compressor and Organizer

This Python application creates structured folders based on the current Jalali (Shamsi) date 📅 and offers options for compressing them into ZIP 🗜️ or TAR.GZ 📦 formats. It simplifies backup workflows with an interactive text-based interface.

## ✨ Features

- **📂 Automatic Folder Creation**: Creates a main folder for the current Jalali date with predefined subfolders.
- **🗜️ Compression Options**: Compresses folders into `.zip` or `.tar.gz` formats with progress tracking.
- **🎛️ Interactive Selection**: Allows users to navigate and select folders using a text-based interface (TUI).
- **🗑️ Safe Deletion**: Offers the option to delete folders after successful compression.
- **📝 Logging**: Logs activities and errors for tracking and debugging.
- **💻 Cross-Platform**: Compatible with Windows, macOS, and Linux.

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/folder-compressor.git
   cd folder-compressor
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # On macOS/Linux
   .\env\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Run the Application**:

   ```bash
   python main.py
   ```

2. **Main Menu Options**:

   - `1. Create Today's Folder with Subfolders`: 📅 Creates a folder named with today's Jalali date and adds predefined subfolders.
   - `2. Select Folder and Compress`: Allows you to select an existing folder and compress it into `.zip` 🗜️ or `.tar.gz` 📦 format.
   - `3. Exit`: 🚪 Exits the application.

3. **Compression Options**:

   - ZIP (Standard 🗜️)
   - TAR.GZ (Compressed 📦)

4. **Optional Deletion**:
   After compression, the application asks if you'd like to delete the original folder 🗑️.

## 📋 Dependencies

- Python 3.7+
- `jdatetime` for Jalali date handling
- `tqdm` for progress bars
- `inquirer` for interactive folder selection
- Standard Python libraries: `os`, `shutil`, `zipfile`, `tarfile`, `logging`

## 📂 Example Folder Structure

If today is `1402-10-05`, the following folder structure will be created:

```
1402-10-05/
├── KaraWeb/
├── Rahkaran/
├── Rahkaran Factory/
├── Vision Factory/
├── Vision Maliati/
└── Vision Pakhsh/
```

## 📝 Logs

- All operations, including errors, are logged in `folder_compressor.log` for debugging and record-keeping.

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
