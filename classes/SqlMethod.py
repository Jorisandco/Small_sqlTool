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
                self.is_mysql_running()
            except Exception as e:
                print(f"Failed to stop MySQL instance: {e}")
        else:
            print("No MySQL instance is running.")
            self.is_mysql_running()

    def is_mysql_running(self):
        if self.process and self.process.poll() is None:
            print("MySQL instance is running.")
        else:
            print("No MySQL instance is running.")