import socket
import threading
from collections import deque


class Server:
    def __init__(self, host, port):
        self.address = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setblocking(False)
        self.sock.bind(self.address)

        self.config = {
            'HOST': host,
            'PORT': port,
            'RECV_BYTES': 1024
        }

        self.received_messages = deque()
        self.outgoing_messages = deque()
        self.messages_needing_ack = deque()

        self.clients = {}
        self.pending_disconnects = []

        self.message_callbacks = {}

        self.running = True

<<<<<<< HEAD
    def update(self):
        pass

=======
>>>>>>> examples
    def message(self, message_id):
        def decorator(f):
            self.message_callbacks[message_id] = f
            return f

        return decorator

    def read_message(self, message, addr):
        message_id = message[:4].decode()
        print(message_id)
        self.message_callbacks[message_id](message)

<<<<<<< HEAD
    def send_message(self, addr):
=======
    def accept_connection(self):
>>>>>>> examples
        pass

    def run(self):
        while self.running:
            try:
                message, addr = self.sock.recvfrom(self.config['RECV_BYTES'])

                if message:
                    print(message)
                    self.read_message(message, addr)
            except Exception:
                pass

    def start(self):
        print('Started server thread.')
        t = threading.Thread(target=self.run)
        t.start()

    def shutdown(self):
        self.sock.close()
        self.running = False