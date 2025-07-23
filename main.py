from generator import input_parser, combiner, leetspeak, case_alter, suffixer, saver
from utils import deduper

def display_banner():
    try:
        with open("logo.txt", "r", encoding="utf-8") as f:
            banner = f.read()
            print(banner)
    except FileNotFoundError:
        print("⚠️ Banner file 'logo.txt' not found.")

def main():
    try:
        display_banner()  # Show the SHAKUNI banner
        
        user_inputs = input_parser.get_inputs()

        if not user_inputs or not any(user_inputs.values()):
            print("❌ No input provided. Please enter at least one field.")
            return

        combos = combiner.generate_combinations(user_inputs)
        leets = leetspeak.transform(combos)
        cases = case_alter.alter_cases(leets)
        suffix = user_inputs.get("suffix", "")
        suffixed = suffixer.append_suffix(cases, suffix)
        final_list = deduper.remove_duplicates(suffixed)

        saver.save_to_file(final_list)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
