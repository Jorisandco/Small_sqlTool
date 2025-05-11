import os
import sys
import ctypes
import subprocess

class SqlMethod:
    def run_as_admin(self, command):
        script = f"""@echo off
{command}
"""
        bat_path = os.path.join(os.getenv("TEMP"), "mysql_admin.bat")
        with open(bat_path, "w") as f:
            f.write(script)

        # Run as admin
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", bat_path, None, None, 1
        )

    def boot_mysql(self):
        self.run_as_admin("net start MySQL80")

    def close_mysql(self):
        self.run_as_admin("net stop MySQL80")

    def detect_mysql(self):
        process = subprocess.Popen(
            "net start",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        output, error = process.communicate()
        return "MySQL80" in output
