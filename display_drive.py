import ctypes
import subprocess
import os

class DisplayDrive:
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.user32.SetProcessDPIAware()
        self.screen_width = self.user32.GetSystemMetrics(0)
        self.screen_height = self.user32.GetSystemMetrics(1)
    
    def optimize_display(self, media_type):
        if media_type == "gaming":
            self.set_resolution(1920, 1080)
            self.set_refresh_rate(144)
        elif media_type == "movie":
            self.set_resolution(2560, 1440)
            self.set_refresh_rate(60)
        elif media_type == "work":
            self.set_resolution(3840, 2160)
            self.set_refresh_rate(60)
        else:
            print("Unknown media type. Please choose from 'gaming', 'movie', or 'work'.")

    def set_resolution(self, width, height):
        print(f"Setting resolution to {width}x{height}")
        subprocess.run(f'DisplaySwitch.exe /extend', shell=True)
        subprocess.run(f'display.exe {width} {height}', shell=True)

    def set_refresh_rate(self, rate):
        print(f"Setting refresh rate to {rate}Hz")
        # This is a placeholder for setting refresh rate, implement as needed
        # Example: subprocess.run(f'someCommandToChangeRefreshRate {rate}', shell=True)

    def get_current_settings(self):
        print(f"Current Resolution: {self.screen_width}x{self.screen_height}")
        # Placeholder for actual refresh rate retrieval
        print(f"Current Refresh Rate: PlaceholderHz")

if __name__ == "__main__":
    dd = DisplayDrive()
    dd.get_current_settings()
    media_type = input("Enter media type (gaming, movie, work): ").strip().lower()
    dd.optimize_display(media_type)