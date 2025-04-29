import argparse
from file_utils import list_files, sample_file_contents
from llm_handler import identify_relevant_files

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer CLI")
    parser.add_argument("--description", type=str, help="Describe the file type to organize")
    parser.add_argument("--target_dir", type=str, help="Path to the folder to scan")

    args = parser.parse_args()

    print(f"[INFO] Scanning directory: {args.target_dir}")
    files = list_files(args.target_dir)

    if not files:
        print("[ERROR] No files found.")
        return

    print(f"[INFO] Found {len(files)} files. Sampling for analysis...")
    samples = sample_file_contents(files, sample_size=3)

    print(f"[INFO] Asking LLM if files are relevant...")
    relevant_files = identify_relevant_files(args.description, samples, files)

    print(f"[RESULT] {len(relevant_files)} relevant files identified:")
    for file in relevant_files:
        print(f"  - {file}")

if __name__ == "__main__":
    main()
