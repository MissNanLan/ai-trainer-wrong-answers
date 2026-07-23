import unittest
import json
from pathlib import Path

from build_unified_question_bank import main, parse_question_bank


class UnifiedQuestionBankTests(unittest.TestCase):
    def test_parse_returns_all_300_questions_with_answer(self):
        questions, issues = parse_question_bank()

        self.assertEqual(300, len(questions))
        self.assertEqual([], issues)
        self.assertEqual(list(range(1, 301)), [question["id"] for question in questions])
        self.assertTrue(all(question["answer"] in "ABCD" for question in questions))
        self.assertTrue(all([option["key"] for option in question["options"]] == list("ABCD") for question in questions))

    def test_generated_payload_has_unique_ids_and_four_options(self):
        main()
        data = json.loads(Path("question-bank-300.json").read_text(encoding="utf-8"))

        self.assertEqual(list(range(1, 301)), [question["id"] for question in data])
        self.assertTrue(all([option["key"] for option in question["options"]] == list("ABCD") for question in data))

    def test_app_contains_complete_and_wrong_entry_modes(self):
        html = Path("index.html").read_text(encoding="utf-8")

        self.assertIn("完整题库", html)
        self.assertIn("错题集", html)
        self.assertIn("initialWrongIds", html)
        self.assertIn("question-bank-300.json", html)


if __name__ == "__main__":
    unittest.main()
