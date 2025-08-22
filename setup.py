# ===== GANESHA KARAOKE COLAB SETUP =====
"""
Quick setup for Ganesha Karaoke project in any Colab account
Run this first in any new Colab session
"""

def quick_setup():
    print("🚀 Setting up Ganesha Karaoke environment...")
    
    # Mount Google Drive
    from google.colab import drive
    drive.mount('/content/drive')
    
    # Install system dependencies
    print("📦 Installing system packages...")
    import os
    os.system('apt-get update > /dev/null 2>&1')
    os.system('apt-get install -y ffmpeg fonts-noto fonts-dejavu > /dev/null 2>&1')
    
    # Install Python packages
    print("🐍 Installing Python packages...")
    os.system('pip install --quiet moviepy pillow numpy')
    
    # Create project structure
    print("📁 Creating project folders...")
    folders = [
        '/content/drive/MyDrive/Ganesha/Images',
        '/content/drive/MyDrive/Ganesha/audio', 
        '/content/drive/MyDrive/Ganesha/output video',
        '/content/drive/MyDrive/Ganesha/json_output'
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    print("✅ Setup complete! Ready for karaoke creation.")
    return True

# Auto-run setup
if __name__ == "__main__":
    quick_setup()
