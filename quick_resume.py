# ===== QUICK RESUME FOR DISCONNECTED SESSIONS =====
"""
Resume karaoke creation after Colab disconnect
Checks for existing work and continues from where left off
"""

def quick_resume():
    print("🔍 Checking for previous work...")
    
    # Check for existing files
    files_to_check = {
        'transcription': '/content/drive/MyDrive/Ganesha/complete_transcription.json',
        'audio': '/content/drive/MyDrive/Ganesha/audio/Shree-Ganesha.mp3',
        'images': '/content/drive/MyDrive/Ganesha/Images'
    }
    
    all_found = True
    for name, path in files_to_check.items():
        if os.path.exists(path):
            print(f"✅ {name}: Found")
        else:
            print(f"❌ {name}: Missing")
            all_found = False
    
    if all_found:
        print("🎉 All files found! Ready to resume video creation.")
        
        # Import and run karaoke builder
        from karaoke_builder import create_video
        create_video()
        
        return True
    else:
        print("⚠️ Some files missing. Please upload required files.")
        return False

if __name__ == "__main__":
    quick_resume()
