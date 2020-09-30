import unittest
from GitHubAPI567 import get_repo_data


class GitHubAPI567TestCase(unittest.TestCase):

    def test_input_validation(self):
        """
        Tests that get_repo_data raises ValueError Execptions for invalid input
        """
        with self.assertRaises(ValueError):
            get_repo_data("     ")
        with self.assertRaises(ValueError):
            get_repo_data("nonExistentUserID")

        self.assertTrue(get_repo_data("derobertsw"))

    def test_get_repo_data(self):
        """
        Tests that get_repo_data returns correct data
        """
        self.assertEqual(get_repo_data("derobertsw"), [("GitHubAPI567", 2), ("ssw567_hw2_triangle", 9), ("Student"
                                                                                                         "-Repository", 42)])

if __name__ == '__main__':
    unittest.main()
