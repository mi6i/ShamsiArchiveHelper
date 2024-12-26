import os
import zipfile
import tarfile
from tqdm import tqdm
import logging

# Logging Configuration
logging.basicConfig(
    filename="logs/folder_compressor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def compress_to_zip_with_progress(source_folder):
    """Compress a folder into a ZIP file with progress."""
    archive_name = f"{os.path.basename(source_folder)}.zip"
    print(f"\n🔄 Compressing folder to ZIP...")

    files_to_compress = [
        os.path.join(root, file)
        for root, _, files in os.walk(source_folder)
        for file in files
    ]

    try:
        with zipfile.ZipFile(archive_name, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in tqdm(files_to_compress, desc="Compressing", unit="file"):
                arcname = os.path.relpath(file, source_folder)
                zipf.write(file, arcname)
        print(f"✅ ZIP compression completed: '{archive_name}'")
        logging.info(f"Compressed '{source_folder}' into '{archive_name}'")
        return archive_name
    except Exception as e:
        print(f"❌ ZIP Compression failed: {e}")
        logging.error(f"ZIP Compression error: {e}")
        return None

def compress_to_tar_with_progress(source_folder):
    """Compress a folder into a TAR.GZ file with progress."""
    archive_name = f"{os.path.basename(source_folder)}.tar.gz"
    print(f"\n🔄 Compressing folder to TAR.GZ...")

    files_to_compress = [
        os.path.join(root, file)
        for root, _, files in os.walk(source_folder)
        for file in files
    ]

    try:
        with tarfile.open(archive_name, "w:gz") as tarf:
            for file in tqdm(files_to_compress, desc="Compressing", unit="file"):
                arcname = os.path.relpath(file, source_folder)
                tarf.add(file, arcname=arcname)
        print(f"✅ TAR.GZ compression completed: '{archive_name}'")
        logging.info(f"Compressed '{source_folder}' into '{archive_name}'")
        return archive_name
    except Exception as e:
        print(f"❌ TAR.GZ Compression failed: {e}")
        logging.error(f"TAR.GZ Compression error: {e}")
        return None
