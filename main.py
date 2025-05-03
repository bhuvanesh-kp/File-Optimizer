import argparse
from file_utils import list_files, sample_file_contents
from llm_handler import identify_relevant_files

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer CLI")
    parser.add_argument("--description", type=str, help="Describe the file type to organize")
    parser.add_argument("--target_dir", type=str, help="Path to the folder to scan")

    args = parser.parse_args()

    if args.description is None:
        print("[ERROR] Please provide a description of the file type to organize.")
        return

    if args.target_dir is None:
        print("[ERROR] Please provide a target directory to scan.")
        return

    print(f"[INFO] Requirement to handle: {args.description}")
    directorys, files = list_files(args.target_dir)

    print(f"[RESULT] {len(directorys)} directorys found:")  # Finding global directorys present in the requeted directory
    print(*directorys, sep="\n")


    print("-" * 20)


    print(f"[RESULT] {len(files)} files found:")  # Finding global files present in the requeted directory
    print(*files, sep="\n")

    '''print(f"[INFO] Found {len(files)} files. Sampling for analysis...")
    samples = sample_file_contents(files, sample_size=3)'''

    print(f"[INFO] File Processing...")
    relevant_files = identify_relevant_files(args.description, files)

    """ print(f"[RESULT] {len(relevant_files)} relevant files identified:")
    for file in relevant_files:
        print(f"  - {file}") """

if __name__ == "__main__":
    main()
