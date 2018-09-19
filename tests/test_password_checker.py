import unittest

from app.password_checker import valid_passwords, display_valid_passwords


class TestPasswordChecker(unittest.TestCase):
    def setUp(self):
        pass

    def test_passwords_with_less_than_6_chars_are_invalid(self):
        self.assertListEqual(valid_passwords('abcde, @Bcd3'), [])

    def test_passwords_with_more_than_12_chars_invalid(self):
        self.assertListEqual(valid_passwords('@Bcd3FahsjrksT'), [])

    def test_is_valid_password(self):
        self.assertListEqual(
            valid_passwords(
                "ABd1234@1,a F1#,2w3E*,2We3345,0ctoFus23@, b@dm1N, b@dm1Ntodsf"
            ),
            ['ABd1234@1', '0ctoFus23@', ' b@dm1N', ' b@dm1Ntodsf']
        )

    def test_white_space_not_allowed_within_password(self):
        self.assertListEqual(valid_passwords('ABd12 34@1'), [])

    def test_display_passwords_output_if_valid(self):
        self.assertEqual(
            display_valid_passwords(
                "ABd1234@1,a F1#,2w3E*,2We3345,0ctoFus23@, b@dm1N, b@dm1Ntodsf"
            ),
            "ABd1234@1, 0ctoFus23@,  b@dm1N,  b@dm1Ntodsf"
        )

    def test_display_if_none_of_given_passwords_is_valid(self):
        self.assertEqual(
            display_valid_passwords(
                "a F1#,2w3E*,2We3345,0ctofus23@, b@dm1n, b@dm1Ntodsfert"
            ),
            "None of the passwords is valid"
        )
