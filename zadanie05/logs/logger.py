import datetime

class Logger:
    log_file='karetki.log'
        
    @staticmethod
    def _log_to_file(message):
        with open(Logger.log_file, 'a') as file:
            file.write(message + '\n')

    @staticmethod
    def _log_to_console(message):
        print(message)

    def log(level, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp} - {level} - {message}"
        
        Logger._log_to_console(formatted_message)
        Logger._log_to_file(formatted_message)

    def info(message):
        Logger.log('INFO', message)

    def debug( message):
        Logger.log('DEBUG', message)

    def warn(message):
        Logger.log('WARN', message)

    def error(message):
        Logger.log('ERROR', message)
        raise ValueError(message)
