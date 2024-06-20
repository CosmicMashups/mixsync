from utils import delay, read_database, bpm_finder, key_finder, sort_bpm, sort_keys

div = "=" * 15
print(f"{div} WELCOME TO MIXSYNC {div}")
print("""With this application, you can accurately find and sort songs by key and BPM,
curated with meticulous verification, and filter them by various attributes for a
seamless music-matching experience.""")

while True:
    surrounding_keys = []
    db_opt = [1, 2]

    while True:
        print(f"{div}===================={div}")
        print("""[1] ANIME      [2] WESTERN""")
        db_name = int(input("Choose the type of song you want to find from [#]: "))
        if db_name in db_opt:
            break
        else:
            print("Invalid option.")
            continue

    match db_name:
        case 1:
            db_name = 'anime.csv'
            # List of keys
            key_list = ["C Major", "C# Major", "D Major", "D# Major", "E Major", "F Major",
                        "F# Major", "G Major", "G# Major", "A Major", "A# Major", "B Major"]
        case 2:
            db_name = 'western.csv'
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

    sort_db = sort_bpm(database, bpm, bpm_thresh)

    # # User input: Ask if the list needs to be sorted
    # sort_option = input("Do you want to sort the list (Yes/No): ").lower()
    # if sort_option == "yes":
    #     sort_column = input(f"How do you want to sort it ({', '.join(columns_to_display)}): ")
    #     sort_db = sorting(sort_column)
    # else:
    #     sort_db = database  # Use the unsorted database

    # Function calls: Find songs
    find_bpm = bpm_finder(sort_db, bpm, bpm_thresh)
    find_keybpm = key_finder(find_bpm, key, key_thresh, key_list)
    sorted_keybpm = sort_keys(find_keybpm, key, key_thresh, key_list)

    # Display results
    delay()
    print(f"{div} SONGS {div}")
    print(sorted_keybpm[columns_to_display])
    print(f"{div}======={div}")

    # User input: Ask if the user wants to run another query
    option = input("Do you still want to search (Yes/No): ").lower()
    if option != "yes":
        delay()
        print("Thank you for using MixSync!")
        break