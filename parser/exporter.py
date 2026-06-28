import json
import csv
import os


class Exporter:

    def export_json(self, result, filename="output/resume.json"):

        os.makedirs("output", exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:

            json.dump(result, f, indent=4)

        print("JSON Exported Successfully")


    def export_csv(self, result, filename="output/resume.csv"):

        os.makedirs("output", exist_ok=True)

        with open(filename, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow(["Field", "Value"])

            for key, value in result.items():

                writer.writerow([key, str(value)])

        print("CSV Exported Successfully")