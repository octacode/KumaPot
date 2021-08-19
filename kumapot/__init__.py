import logging
import threading
from socket import socket, timeout


class HoneyPot(object):
    def __init__(self, ports, log_filepath, host):
        self.ports = ports
        self.log_filepath = log_filepath
        self.listener_thread = {}
        self.host = host
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%s',
                            filename=self.log_filepath,
                            filemode='w')
        # Console logging configuration
        self.logger = logging.getLogger(__name__)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        self.logger.addHandler(console_handler)
        if len(ports) < 1:
            print('No ports found')
            raise Exception('No ports provided')
        self.logger.info('Honeypot initializing')
        self.logger.info('Ports %s' % self.ports)
        self.logger.info('Logfile path %s' % self.log_filepath)

    def handle_connection(self, client_socket, port, ip, remote_port):
        self.logger.info('Connection received %s from %s:%d' % (port, ip, remote_port))
        client_socket.settimeout(10)
        try:
            data = client_socket.recv(1000)
            self.logger.info('Connection on %s from %s:%d - %s' %(port, ip, remote_port, data))
            client_socket.send('Access Denied!!'.encode('utf8'))
        except timeout:
            pass
        client_socket.close()

    def start_new_listener_thread(self, port):
        listener = socket()
        listener.bind((self.host, int(port)))
        listener.listen(5)
        while True:
            client, addr = listener.accept()
            client_handler = threading.Thread(target=self.handle_connection, args=(client, port, addr[0], addr[1]))
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