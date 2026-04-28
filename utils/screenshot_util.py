import os
import time
from datetime import datetime

class ScreenshotUtil:

    def __init__(self, base_dir="screenshots"):
        self.base_dir = base_dir

        # 🔥 Create ONE folder per run
        self.run_timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        self.run_folder = os.path.join(self.base_dir, self.run_timestamp)

        # Create base + run folder
        os.makedirs(self.run_folder, exist_ok=True)

    def _get_path(self, name):
        timestamp = datetime.now().strftime("%H-%M-%S")
        return os.path.join(self.run_folder, f"{name}_{timestamp}.png")

    def capture(self, driver, name="screenshot"):
        file_path = self._get_path(name)

        try:
            import pyautogui
            time.sleep(1)

            # Ensure browser is focused
            driver.switch_to.window(driver.current_window_handle)
            time.sleep(0.5)

            screenshot = pyautogui.screenshot()
            screenshot.save(file_path)

            print(f"[INFO] Screenshot saved: {file_path}")

        except Exception as e:
            print(f"[WARNING] PyAutoGUI failed: {e}")
            self._fallback(file_path)

    def _fallback(self, file_path):
        try:
            import mss
            with mss.mss() as sct:
                sct.shot(output=file_path)

            print(f"[INFO] Screenshot saved using MSS: {file_path}")

        except Exception as e:
            print(f"[CRITICAL] Screenshot failed: {e}")