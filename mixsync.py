import pandas as pd
import time

# Read the database based on db_name
def read_database(db_name):
    if db_name.lower() == 'keybpm.csv':
        database = pd.read_csv('keybpm.csv')
        columns_to_display = ['BPM', 'TITLE', 'KEY', 'YEAR']
    elif db_name.lower() == 'westerndb.csv':
        database = pd.read_csv('westerndb.csv')
        columns_to_display = ['ARTIST', 'TITLE', 'KEY', 'BPM']
    else:
        raise ValueError("Unsupported database name")

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    return database, columns_to_display


# Delay function for animation purposes
def delay():
    time.sleep(0.5)


# Check if input is numeric
def is_numeric(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False


# Sort database by specified column
def sorting(sort_column):
    sort_order = input("Ascending or Descending? [A/D]: ")
    if sort_order.lower() == "a":
        sorted_df = database.sort_values(by=sort_column)
    elif sort_order.lower() == "d":
        sorted_df = database.sort_values(by=sort_column, ascending=False)
    sorted_df.to_csv(db_name, index=False)
    return sorted_df


# Find songs within specified BPM range
def bpm_finder(database, bpm, bpm_thresh):
    delay()
    print(f"Finding songs that are ±{bpm_thresh} BPM around {bpm} BPM...")
    bpm_min = bpm - bpm_thresh
    bpm_max = bpm + bpm_thresh
    find_bpm = database[(database['BPM'].between(bpm_min, bpm_max))]
    return find_bpm


# Find songs within specified key range
def key_finder(find_bpm, key, key_thresh):
    delay()
    print(f"Finding songs that are {key_thresh} keys apart from {key}...")
    key_index = key_list.index(key)
    surrounding_keys = []
    for counter in range(-key_thresh, key_thresh + 1):
        if 0 <= key_index + counter < len(key_list):
            surrounding_keys.append(key_list[key_index + counter])
    find_keybpm = find_bpm[find_bpm['KEY'].isin(surrounding_keys)]
    return find_keybpm


# MAIN PROGRAM
if __name__ == "__main__":
    div = "=" * 15
    print(f"{div} WELCOME TO MIXSYNC {div}")
    print("""With this application, you can accurately find and sort songs by key and BPM,
curated with meticulous verification, and filter them by various attributes for a
seamless music-matching experience.""")

    while True:
        print(f"{div}===================={div}")
        surrounding_keys = []
        print("""[1] ANIME      [2] WESTERN""")

        db_name = int(input("Choose the type of song you want to find from [#]: "))

        match db_name:
            case 1:
                db_name = 'keybpm.csv'
                # List of keys
                key_list = ["C Major", "C# Major", "D Major", "D# Major", "E Major", "F Major",
                            "F# Major", "G Major", "G# Major", "A Major", "A# Major", "B Major"]
            case 2:
                db_name = 'westerndb.csv'
                # List of keys
                key_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        try:
            database, columns_to_display = read_database(db_name)
        except ValueError as e:
            print(e)
            exit()

        # User input: BPM, Key, BPM and Key Threshold
        while True:
            try:
                bpm = int(input("Specify the BPM (#): "))
                if bpm not in range(70, 140):
                    raise ValueError("BPM must be between 70 and 139.")
                break
            except ValueError:
                print("Input is not a valid number or outside the range.")

        while True:
            key = input("Specify the Key: ")
            if key in key_list:
                break
            else:
                print("Input is not a valid key.")

        while True:
            try:
                bpm_thresh = int(input("Specify the BPM Gap (#): "))
                break
            except ValueError:
                print("Input is not a valid number.")

        while True:
            try:
                key_thresh = int(input("Specify the Key Gap (#): "))
                break
            except ValueError:
                print("Input is not a valid number.")

        # Adjust bpm and bpm_thresh if bpm is not in the range
        if bpm not in range(70, 140):
            bpm /= 2
            bpm_thresh /= 2

        # User input: Ask if the list needs to be sorted
        sort_option = input("Do you want to sort the list (Yes/No): ").lower()
        if sort_option == "yes":
            sort_column = input(f"How do you want to sort it ({', '.join(columns_to_display)}): ")
            sort_db = sorting(sort_column)
        else:
            sort_db = database  # Use the unsorted database

        # Function calls: Find songs
        find_bpm = bpm_finder(sort_db, bpm, bpm_thresh)
        find_keybpm = key_finder(find_bpm, key, key_thresh)

        # Display results
        delay()
        print(f"{div} SONGS {div}")
        print(find_keybpm[columns_to_display])
        print(f"{div}======={div}")

        # User input: Ask if the user wants to run another query
        option = input("Do you still want to search (Yes/No): ").lower()
        if option != "yes":
            delay()
            print("Thank you for using MixSync!")
            break
