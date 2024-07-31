import unittest
from unittest.mock import patch, MagicMock
from logs import Logger 
import datetime

# testy można wywołać ręcznie w terminalu komendą:
# python -m unittest ./tests/<plik>.py

class TestLogger(unittest.TestCase):

    @patch('logs.Logger._log_to_console')
    @patch('logs.Logger._log_to_file')
    def test_log_methods(self, mock_log_to_file, mock_log_to_console):
        # Testowanie metody log()
        Logger.log('INFO', 'This is a test message')

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp} - INFO - This is a test message"

        mock_log_to_console.assert_called_once_with(formatted_message)

        mock_log_to_file.assert_called_once_with(formatted_message)

    @patch('logs.Logger._log_to_console')
    @patch('logs.Logger._log_to_file')
    def test_info(self, mock_log_to_file, mock_log_to_console):
        Logger.info('Info message')

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp} - INFO - Info message"

        mock_log_to_console.assert_called_once_with(formatted_message)
        mock_log_to_file.assert_called_once_with(formatted_message)

    @patch('logs.Logger._log_to_console')
    @patch('logs.Logger._log_to_file')
    def test_debug(self, mock_log_to_file, mock_log_to_console):
        Logger.debug('Debug message')

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp} - DEBUG - Debug message"

        mock_log_to_console.assert_called_once_with(formatted_message)
        mock_log_to_file.assert_called_once_with(formatted_message)

    @patch('logs.Logger._log_to_console')
    @patch('logs.Logger._log_to_file')
    def test_warn(self, mock_log_to_file, mock_log_to_console):
        Logger.warn('Warning message')

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp} - WARN - Warning message"

        mock_log_to_console.assert_called_once_with(formatted_message)
        mock_log_to_file.assert_called_once_with(formatted_message)

    @patch('logs.Logger._log_to_console')
    @patch('logs.Logger._log_to_file')
    def test_error(self, mock_log_to_file, mock_log_to_console):
        with self.assertRaises(ValueError):
            Logger.error('Error message')

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp} - ERROR - Error message"

        mock_log_to_console.assert_called_once_with(formatted_message)
        mock_log_to_file.assert_called_once_with(formatted_message)

if __name__ == '__main__':
    unittest.main()
