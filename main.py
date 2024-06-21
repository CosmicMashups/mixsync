from match import delay, read_database, song_match      # bpm_finder, key_finder, sort_bpm, sort_keys
from search import search_song                          # sorting

div = "=" * 15
print(f"{div} WELCOME TO MIXSYNC {div}")
print("""With this application, you can accurately find and sort songs by key and BPM,
curated with meticulous verification, and filter them by various attributes for a
seamless music-matching experience.""")

while True:
    surrounding_keys = []
    db_opt = [1, 2, 3, 4]
    process_opt = [1, 2, 3, 4]

    while True:
        print(f"{div} SONG TYPE {div}")
        print("""[1] ANIME      [3] K-POP""")
        print("""[2] WESTERN    [4] OPM""")
        db_name = int(input("Select the song type you wish to search from [#]: "))
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
        case 3:
            print("We're sorry. The database containing K-Pop songs is still not ready yet.")
            break
        case 4:
            print("We're sorry. The database containing OPM songs is still not ready yet.")
            break

    try:
        database, columns_to_display = read_database(db_name)
    except ValueError as e:
        print(e)
        exit()

    while True:
        print(f"{div} PROCESS {div}")
        print("""[1] SEARCH             [3] MATCH (BY KEY, BPM)""")
        print("""[2] ADD SONGS          [4] MATCH (BY SONG)""")
        process = int(input("Which procedure would you like to perform [#]: "))
        if process in process_opt:
            break
        else:
            print("Invalid option.")
            continue

    match process:
        # SEARCH
        case 1:
            searched = search_song(database, db_name, columns_to_display, div)

            if searched is not None and not searched.empty:
                searched_title = searched.iloc[0]['TITLE']
                search_match = input(f"Do you want to search songs that would match '{searched.iloc[0]['TITLE']}' by '{searched.iloc[0]['ARTIST']}' [Y/N]: ").lower()

                if search_match == "y":
                    bpm = int(searched.iloc[0]['BPM'])
                    key = searched.iloc[0]['KEY']
                    song_match(database, bpm, key, key_list, columns_to_display, div)
                else:
                    print("No search performed.")

            else:
                print("No search performed.")

        # ADD SONGS
        case 2:
            print("We're sorry. The feature of adding songs is still not available.")
            break

        # MATCH (BY KEY, BPM)
        case 3:
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

            song_match(database, bpm, key, key_list, columns_to_display, div)

        # MATCH (BY SONG)
        case 4:
            print("We're sorry. The feature of matching songs by a specific song is still not available.")
            break

    # User input: Ask if the user wants to run another query
    option = input("Do you still want to search (Yes/No): ").lower()
    if option != "yes":
        delay()
        print("Thank you for using MixSync!")
        break
