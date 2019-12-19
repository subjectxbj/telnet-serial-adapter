import serial
class Serial:
	def __init__(self):
		pass
		
	def connect(self, com="COM3", bitrate=115200):
		self.m_serial = serial.Serial(com, bitrate, timeout=0.5)
		self.m_buffer_size = 8000

	def write(self, message):
		self.m_serial.write(message.encode("utf-8"))

	def read(self):
		return self.m_serial.read(self.m_buffer_size).decode("utf-8")

	def cmd(self, command, delay=0):
		from time import sleep
		if (command.find('\n') < 0):
			self.write(command+"\n")
		else:
			self.write(command)
		if (delay > 0):
			sleep(delay)
		return self.read()

	def close(self):
		self.m_serial.close()