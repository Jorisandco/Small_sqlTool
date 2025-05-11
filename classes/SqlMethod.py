import subprocess

class SqlMethod:
    def __init__(self, mysql_path="C:/Program Files/MySQL/MySQL Server 8.0/bin/mysqld.exe"):
        self.mysql_path = mysql_path
        self.process = None

    def boot_mysql(self):
        try:
            self.process = subprocess.Popen([self.mysql_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("MySQL instance started.")
        except Exception as e:
            print(f"Failed to start MySQL instance: {e}")

    def close_mysql(self):
        if self.process:
            try:
                self.process.terminate()
                self.process.wait()
                print("MySQL instance stopped.")
            except Exception as e:
                print(f"Failed to stop MySQL instance: {e}")
        else:
            print("No MySQL instance is running.")