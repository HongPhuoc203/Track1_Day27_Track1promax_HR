"""Evaluate Auto-CV Screener predictions against the Golden Cases."""
import argparse
import json
from pathlib import Path


def load_json(path):
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def evaluate(golden, predictions):
    by_id = {item["id"]: item for item in predictions}
    rows = []
    for case in golden:
        prediction = by_id.get(case["id"], {})
        predicted = prediction.get("predicted_tier", "MISSING")
        expected = case["expected_tier"]
        rows.append({"id": case["id"], "expected": expected, "predicted": predicted,
                     "correct": predicted == expected,
                     "false_negative": expected in {"Tier 1", "Tier 2"} and predicted == "Tier 3"})
    total = len(rows)
    matches = sum(row["correct"] for row in rows)
    eligible = sum(case["expected_tier"] in {"Tier 1", "Tier 2"} for case in golden)
    false_negatives = sum(row["false_negative"] for row in rows)
    return rows, {"total": total, "matches": matches,
                  "match_rate": round(matches / total * 100, 2) if total else 0,
                  "false_negatives": false_negatives,
                  "false_negative_rate": round(false_negatives / eligible * 100, 2) if eligible else 0}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions")
    parser.add_argument("--golden", default="eval_golden_dataset.json")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    golden = load_json(args.golden)
    if args.self_test:
        predictions = [{"id": c["id"], "predicted_tier": c["expected_tier"]} for c in golden]
    elif args.predictions:
        predictions = load_json(args.predictions)
    else:
        parser.error("provide --predictions predictions.json or use --self-test")
    _, metrics = evaluate(golden, predictions)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
