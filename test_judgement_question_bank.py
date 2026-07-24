import json
import unittest

from build_judgement_question_bank import parse_question_bank


class JudgementQuestionBankTests(unittest.TestCase):
    def test_parses_all_questions_with_answers_and_explanations(self):
        questions, issues = parse_question_bank()
        self.assertEqual([], issues)
        self.assertEqual(list(range(1, 301)), [q["id"] for q in questions])
        self.assertTrue(all(q["answer"] in {"√", "×"} for q in questions))
        self.assertTrue(all(q["stem"] and q["note"] for q in questions))

    def test_generated_json_matches_parsed_question_bank(self):
        questions, _ = parse_question_bank()
        with open("judgement-bank-300.json", encoding="utf-8") as fh:
            saved = json.load(fh)
        self.assertEqual(questions, saved)


if __name__ == "__main__":
    unittest.main()
