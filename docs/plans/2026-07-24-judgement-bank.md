# Judgement Bank Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a separate 300-question judgement-practice entry with √/× answers, original explanations, independent progress, and an editable wrong-question set.

**Architecture:** Parse the supplied Word question and answer-analysis documents into `judgement-bank-300.json`. Add `judgement.html` as a standalone static page that mirrors the existing offline practice behavior while storing all judgement-specific state under its own localStorage key. Add links between the single-choice and judgement pages.

**Tech Stack:** Static HTML/CSS/JavaScript, Python `python-docx`, JSON, GitHub Pages.

---

### Task 1: Parse and validate judgement data

**Files:**
- Create: `build_judgement_question_bank.py`
- Create: `test_judgement_question_bank.py`
- Create: `judgement-bank-300.json`

**Step 1: Write the failing test**

Assert that parsing returns exactly IDs 1–300, each entry has a non-empty stem, an answer of √ or ×, and a non-empty source explanation.

**Step 2: Run test to verify it fails**

Run: `python3 test_judgement_question_bank.py`
Expected: FAIL because parser and JSON are absent.

**Step 3: Write minimal parser**

Read the numbered question paragraphs from `人工智能训练师三级_判断题题目 1-300.docx`; read rows 1–200 from the two answer tables; read 201–300 from paragraph blocks containing `答案：` and `解析：`; emit JSON only when all IDs and explanations are present.

**Step 4: Run parser and tests**

Run: `python3 build_judgement_question_bank.py && python3 test_judgement_question_bank.py`
Expected: 300 questions generated and all tests pass.

**Step 5: Commit**

```bash
git add build_judgement_question_bank.py test_judgement_question_bank.py judgement-bank-300.json
git commit -m "feat: add judgement question data"
```

### Task 2: Create independent judgement practice page

**Files:**
- Create: `judgement.html`
- Modify: `index.html`
- Test: `test_judgement_page.py`

**Step 1: Write the failing test**

Assert the page fetches `judgement-bank-300.json`, has √ and × answer buttons, renders the explanation after submission, and uses a judgement-only localStorage key for full and wrong-set records.

**Step 2: Run test to verify it fails**

Run: `python3 test_judgement_page.py`
Expected: FAIL because `judgement.html` is absent.

**Step 3: Implement the page**

Reuse the interaction model of the single-choice page: complete bank/wrong set, independent review records, persistent wrong IDs, manual remove from wrong set, uncertain flag, jump by ID, answer correction, export, and reset that preserves answer corrections plus wrong-set membership. Use the source explanation in the feedback panel.

**Step 4: Add reciprocal navigation**

Add a visible link on the existing single-choice page to `judgement.html`, and a link back on the judgement page to `index.html`.

**Step 5: Run page test and syntax checks**

Run: `python3 test_judgement_page.py && sed -n 's#.*<script>##; s#</script>.*##p' judgement.html | node --check /dev/stdin`
Expected: PASS.

**Step 6: Commit**

```bash
git add judgement.html index.html test_judgement_page.py
git commit -m "feat: add judgement practice page"
```

### Task 3: Full verification and deployment

**Files:**
- Verify: `index.html`, `judgement.html`, `question-bank-300.json`, `judgement-bank-300.json`

**Step 1: Run all tests**

Run: `python3 test_unified_question_bank.py && python3 test_judgement_question_bank.py && python3 test_judgement_page.py`
Expected: all tests pass.

**Step 2: Check generated data and JavaScript syntax**

Run: `python3 build_judgement_question_bank.py && sed -n 's#.*<script>##; s#</script>.*##p' index.html | node --check /dev/stdin && sed -n 's#.*<script>##; s#</script>.*##p' judgement.html | node --check /dev/stdin && git diff --check`
Expected: 300 validated judgement items and no syntax/diff errors.

**Step 3: Merge and deploy**

Merge the verified feature branch into `main`, then `git push origin main`; GitHub Pages publishes from `main` automatically.
