import unittest
from unittest import mock
from typing import List

from GitHubAPI567 import get_repo_data, get_repo_name_json, get_repo_list


class GitHubAPI567TestCase(unittest.TestCase):

    @mock.patch('requests.get')
    def test_input_validation(self, mocked_req):
        """
        Tests that get_repo_data raises ValueError Exceptions for invalid input
        """
        mocked_req.return_value.status_code = 404

        with self.assertRaises(ValueError):
            get_repo_data("     ")
        with self.assertRaises(ValueError):
            get_repo_data("nonExistentUserID")

    @mock.patch('requests.get')
    def test_get_repo_json_data(self, mocked_req):
        """
        Tests that get_repo_data returns correct data
        """
        mocked_req.return_value.status_code = 200
        mocked_req.return_value.json.return_value = [{'name': 'GitHubAPI567'},
                                                     {'name': 'home'},
                                                     {'name': 'ssw567_hw2_triangle'},
                                                     {'name': 'ssw567_triangle'},
                                                     {'name': 'Student-Repository'}]

        self.assertEqual(get_repo_name_json("derobertsw"),
                         [{'name': 'GitHubAPI567'},
                          {'name': 'home'},
                          {'name': 'ssw567_hw2_triangle'},
                          {'name': 'ssw567_triangle'},
                          {'name': 'Student-Repository'}])

    @mock.patch('requests.get')
    def test_get_repo_list(self, mocked_req):
        mocked_req.return_value.json.return_value = [1, 2, 3, 4]

        repos: List = [{'name': 'GitHubAPI567'},
                       {'name': 'home'},
                       {'name': 'ssw567_hw2_triangle'},
                       {'name': 'ssw567_triangle'},
                       {'name': 'Student-Repository'}]

        self.assertEqual(get_repo_list("derobertsw", repos),
                         [('GitHubAPI567', 4), ('home', 4), ('ssw567_hw2_triangle', 4), ('ssw567_triangle', 4),
                          ('Student-Repository', 4)])


if __name__ == '__main__':
    unittest.main()
