import logging
import threading
from socket import socket


class HoneyPot(object   ):
    def __init__(self, ports, log_filepath):
        self.ports = ports
        self.log_filepath = log_filepath
        self.listener_thread = {}
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%s',
                            filename=self.log_filepath,
                            filemode='w')
        self.logger = logging.getLogger(__name__)
        if len(ports) < 1:
            print('No ports found')
            raise Exception('No ports provided')
        self.logger.info('Honeypot initializing')
        self.logger.info('Ports %s' % self.ports)
        self.logger.info('Logfile path %s' % self.log_filepath)

    def handle_connection(self, client_socket, ip, remote_port):
        data = client_socket.recv(1000)
        self.logger.info('Connection from %s:%d - %s' %(ip, remote_port, data))
        client_socket.send('Access Denied!!'.encode('utf8'))
        client_socket.close()

    def start_new_listener_thread(self, port, BIND_IP='0.0.0.0'):
        listener = socket()
        listener.bind((BIND_IP, int(port)))
        listener.listen(5)
        while True:
            client, addr = listener.accept()
            client_handler = threading.Thread(target=self.handle_connection, args=(client, addr[0], addr[1]))
            client_handler.start()

    def start_listening(self):
        for port in self.ports:
            self.logger.info('Started listening to %s' % port)
            self.listener_thread[port] = threading.Thread(target=self.start_new_listener_thread, args=(port,))
            self.listener_thread[port].start()

    def run(self):
        self.start_listening()
        while True:
            pass