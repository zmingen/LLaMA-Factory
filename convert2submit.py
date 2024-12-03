import json
from pathlib import Path
import pandas as pd
import argparse

def convert2submit(test_file: Path, prediction_file: Path, save_path: Path):
    pred_label_list = []

    for line in open(prediction_file, "r"):
        prediction_data = json.loads(line)
        pred_label = prediction_data["predict"]
        pred_label_list.append(pred_label)

    test_data = json.load(open(test_file, "r"))
    save_data = []
    for i, example in enumerate(test_data):
        example["predict"] = pred_label_list[i]
        save_data.append(example)

    df = pd.DataFrame(save_data)
    df.to_csv(save_path, index=None, encoding="utf-8-sig")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert test and prediction files to submission format.")
    parser.add_argument("--test_file", type=str, required=True, help="Path to the test file (JSON).")
    parser.add_argument("--prediction_file", type=str, required=True, help="Path to the prediction file (JSONL).")
    parser.add_argument("--save_path", type=str, required=True, help="Path to save the output CSV file.")

    args = parser.parse_args()

    convert2submit(Path(args.test_file), Path(args.prediction_file), Path(args.save_path))