import logging

class HoneyPot(object   ):
    def __init__(self, ports, log_filepath):
        self.ports = ports
        self.log_filepath = log_filepath
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%s',
                            filename=self.log_filepath,
                            filemode='w')
        self.logger = logging.getLogger(__name__)
        self.logger.info('TEST')
        if len(ports) < 1:
            print('No ports found')
            raise Exception('No ports provided')
        self.logger('Honeyport intializingg')

    def start_listening(self):
        for port in self.ports:
            self.logger.info('Started listening to %s' %port)