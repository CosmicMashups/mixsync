from match import delay, read_database, song_match      # bpm_finder, key_finder, sort_bpm, sort_keys
from search import search_song                          # sorting
from add import add_song

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
            db_title = 'Anime'
            db_name = 'anime.csv'
            # List of keys
            key_list = ["C Major", "C# Major", "D Major", "D# Major", "E Major", "F Major",
                        "F# Major", "G Major", "G# Major", "A Major", "A# Major", "B Major"]
        case 2:
            db_title = 'Western'
            db_name = 'western.csv'
            # List of keys
            key_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        case 3:
            db_title = 'K-Pop'
            print(f"We're sorry. The database containing {db_title} songs is still not ready yet.")
            break
        case 4:
            db_title = 'OPM'
            print(f"We're sorry. The database containing {db_title} songs is still not ready yet.")
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
                for counter in range(len(searched.index)):
                    searched_title = searched.iloc[counter]['TITLE']
                    search_match = input(f"Search songs that would match '{searched.iloc[counter]['TITLE']}' by '{searched.iloc[counter]['ARTIST']}'? [Y/N]: ").lower()

                    if search_match == "y":
                        bpm = int(searched.iloc[counter]['BPM'])
                        key = searched.iloc[counter]['KEY']
                        song_match(database, bpm, key, key_list, columns_to_display, div)
                    else:
                        print("No search performed.")

            else:
                print("No search performed.")

        # ADD SONGS
        case 2:
            add_song(database, db_name, db_title, key_list)

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
    option = input("Make another process [Y/N]: ").lower()
    if option != "y":
        delay()
        print("Thank you for using MixSync!")
        break
