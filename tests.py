import unittest
from mock import patch
from person import Person

class TestPersonClass(unittest.TestCase):
    @patch('person.Person.get_unique_id')
    def test_get_unique_id_1(self, mock_get_unique_id):
        """This example is using patch in a decorator approach."""

        # mocking the return value
        mock_get_unique_id.return_value = 12
        # make a call to mock function
        unique_id = Person().get_unique_id()
        assert unique_id == 12

    def test_get_unique_id_2(self):
        """This example is uses patch in a context manager approach."""
        with patch.object(Person, "get_unique_id") as mock_get_unique_id:
            # mocking the return value
            mock_get_unique_id.return_value = 15
             # make a call to mock function
            unique_id = Person().get_unique_id()
            assert  unique_id == 15
