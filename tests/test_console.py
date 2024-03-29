from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(TestCase):
    """
        Unittests for command line interpreter of project.
    """

    def setUp(self):
        """ Setup of interpreter """
        self.interpreter = HBNBCommand()

    def test_emptyline(self):
        """ If input is emptyline """
        with patch("sys.stdout", new=StringIO()) as f:
            self.interpreter.onecmd('\n')
            self.assertEqual("", f.getvalue())
