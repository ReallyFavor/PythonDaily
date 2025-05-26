import os
import sys
import time
from typing import List, Optional
from dataclasses import dataclass
import subprocess
import yaml
from pynput import mouse, keyboard
from pynput.mouse import Controller, Button
from screeninfo import get_monitors

# 常量定义
CONFIG_FILE = 'config.yaml'
DEFAULT_SERVER_CHOICE = 2
DEFAULT_DEVICE_RANGE = "101-110"
CLICK_DELAY = 0.03

# 获取屏幕比例
monitor = get_monitors()[0]
SCREEN_RATIO = {
    'width': monitor.width / 1512,
    'height': monitor.height / 982
}


@dataclass
class Device:
    """设备类，存储设备ID和标题"""
    id: str
    title: str


class DeviceManager:
    """设备管理类"""

    def __init__(self):
        self.config = self._load_config()
        self.all_devices = self.config["all_devices"]
        self.servers = self.config["adb_servers"]
        self.open_device_count = 10

    def _load_config(self) -> dict:
        """加载配置文件"""
        app_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(app_path, CONFIG_FILE)
        try:
            with open(config_path, 'r', encoding="utf-8") as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            sys.exit(1)

    def get_adb_devices(self) -> List[Device]:
        """获取ADB设备列表"""
        try:
            result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, check=True)
            lines = result.stdout.decode('utf-8').splitlines()
            devices = []
            for line in lines[1:]:
                if not line.strip():
                    continue
                parts = line.split('\t')
                if len(parts) == 2:
                    title = self.all_devices.get(parts[0])
                    if title:
                        devices.append(Device(parts[0], title))
            return devices
        except subprocess.CalledProcessError:
            print("执行ADB命令失败")
            return []

    def process_input(self, user_input: str) -> List[int]:
        """处理用户输入"""
        if not user_input:
            return []

        try:
            if any(sep in user_input for sep in [',', '，']):
                return [int(num.strip()) for num in user_input.replace('，', ',').split(',')]
            elif '-' in user_input:
                start, end = map(int, user_input.split('-'))
                return list(range(start, end + 1))[:10]
            return [int(user_input)]
        except ValueError:
            print("输入格式错误")
            return []


class ScrcpyLauncher:
    """Scrcpy启动器类"""

    def __init__(self, device_manager: DeviceManager):
        self.device_manager = device_manager
        self.mouse_controller = Controller()

    def launch_devices(self) -> int:
        """启动设备"""
        print("\n".join(f"选择{server}，请输入{i}" for i, server in enumerate(self.device_manager.servers, 1)))

        server_choice = input(f"请输入要选择的adb server(默认为{DEFAULT_SERVER_CHOICE})：").strip()
        server_index = int(server_choice) if server_choice else DEFAULT_SERVER_CHOICE
        server = self.device_manager.servers[server_index - 1]

        os.environ['ADB_SERVER_SOCKET'] = f"tcp:{server}"
        devices = self.device_manager.get_adb_devices()
        devices.sort(key=lambda x: x.title)

        print("\n设备列表:")
        for device in devices:
            print(f"{device.title}, {device.id}")

        device_input = input(f"请输入你想要打开的设备号(默认{DEFAULT_DEVICE_RANGE}):")
        selected_numbers = self.device_manager.process_input(device_input) if device_input else \
            self.device_manager.process_input(DEFAULT_DEVICE_RANGE)

        selected_devices = [device for device in devices if device.title in selected_numbers]
        if not selected_devices:
            selected_devices = devices[1:11]

        self._launch_scrcpy(selected_devices, server)
        return len(selected_devices)

    def _launch_scrcpy(self, devices: List[Device], server: str):
        """启动scrcpy进程"""
        window_width = get_monitors()[0].width
        for i, device in enumerate(devices):
            x = window_width / 5 * (i % 5)
            y = i // 5 * 540 * SCREEN_RATIO['height']
            cmd = (f"scrcpy --tunnel-host {server.split(':')[0]} -s {device.id} "
                   f"--window-title {device.title} --window-x {int(x)} --window-y {int(y)} "
                   f"-b 2M -m 800 --max-fps 15 --window-height={int(440 * SCREEN_RATIO['height'])} "
                   f"--always-on-top --legacy-paste")
            subprocess.Popen(cmd, shell=True)
            time.sleep(5)


def main():
    device_manager = DeviceManager()
    launcher = ScrcpyLauncher(device_manager)
    device_count = launcher.launch_devices()

    def on_press(key):
        if hasattr(key, 'char') and key.char == '`':
            x, y = launcher.mouse_controller.position
            for count in range(device_count):
                new_x = x + (count % 5) * 302 * SCREEN_RATIO['width']
                new_y = y + (count // 5) * 472 * SCREEN_RATIO['height']
                launcher.mouse_controller.position = (new_x, new_y)
                time.sleep(CLICK_DELAY)
                launcher.mouse_controller.click(Button.left)
                time.sleep(CLICK_DELAY)
            launcher.mouse_controller.position = (x, y)

    print("在第一台打开的设备上按下control键,会自动点击当前鼠标位置以及同时打开的其他设备的相同位置")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
