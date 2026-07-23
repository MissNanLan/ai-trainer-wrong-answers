import unittest

from build_unified_question_bank import parse_question_bank


class UnifiedQuestionBankTests(unittest.TestCase):
    def test_parse_returns_all_300_questions_with_answer(self):
        questions, issues = parse_question_bank()

        self.assertEqual(300, len(questions))
        self.assertEqual([], issues)
        self.assertEqual(list(range(1, 301)), [question["id"] for question in questions])
        self.assertTrue(all(question["answer"] in "ABCD" for question in questions))
        self.assertTrue(all([option["key"] for option in question["options"]] == list("ABCD") for question in questions))


if __name__ == "__main__":
    unittest.main()
