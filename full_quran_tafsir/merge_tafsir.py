"""
Optional Helper Script: Merge split Tafsir parts into single JSON files locally.
Usage:
    python merge_tafsir.py
"""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MANIFEST_PATH = os.path.join(SCRIPT_DIR, "split_tafsir_manifest.json")

def merge():
    if not os.path.exists(MANIFEST_PATH):
        print("split_tafsir_manifest.json not found.")
        return

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    for base_name, info in manifest.items():
        lang = info["language"]
        parts = info["parts"]
        merged_surahs = []
        print(f"Merging {len(parts)} parts for {base_name} ({lang})...")
        for p in parts:
            part_file = os.path.join(SCRIPT_DIR, lang, p["filename"])
            if not os.path.exists(part_file):
                print(f"  Warning: missing {part_file}")
                continue
            with open(part_file, "r", encoding="utf-8") as pf:
                surahs = json.load(pf)
                merged_surahs.extend(surahs)
        
        out_file = os.path.join(SCRIPT_DIR, lang, f"{base_name}.json")
        with open(out_file, "w", encoding="utf-8") as out:
            json.dump(merged_surahs, out, ensure_ascii=False, indent=2)
        sz_mb = os.path.getsize(out_file) / (1024 * 1024)
        print(f"  -> Generated {out_file} ({sz_mb:.2f} MB, {len(merged_surahs)} surahs)")

if __name__ == "__main__":
    merge()

