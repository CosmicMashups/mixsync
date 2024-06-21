import pandas as pd
from match import delay

def add_song(database, db_name, db_title, key_list):
    print(f"You are adding a new record in the '{db_title}' database...")
    avail_column = database.columns.values
    print(f"SEARCH FIELDS: {avail_column}")

    while True:
        song_dl = {}
        for counter in range(len(avail_column)):
            while True:
                if avail_column[counter] != 'TYPE':
                    song_data = input(f"Enter {avail_column[counter]}: ")
                else:
                    song_data = db_title

                if avail_column[counter] == 'KEY':
                    if song_data not in key_list:
                        print("Invalid key.")
                        continue
                    else:
                        break

                elif avail_column[counter] == 'BPM':
                    song_data = int(song_data)
                    while True:
                        if song_data < 70:
                            song_data *= 2
                        elif song_data >= 140:
                            song_data /= 2
                        elif 70 < song_data < 140:
                            break
                    break

                elif avail_column[counter] == 'YEAR':
                    song_data = int(song_data)
                    while True:
                        if 0 < song_data:
                            break
                        else:
                            print("Invalid year.")
                            continue
                    break

                else:
                    break

            song_dl[avail_column[counter]] = song_data
            print(song_dl)

        for item in range(len(avail_column)):
            current_col = avail_column[item]
            current_data = song_dl[current_col]
            print(f"[{item + 1}] {current_col}: {current_data}")

        new_data = pd.DataFrame([song_dl])
        data_check = input("Is this correct [Y/N]: ").lower()

        if data_check == "y":
            updated_df = pd.concat([database, new_data], ignore_index=True)
            updated_df.to_csv(db_name, index=False)

        else:
            data_confirm = input("Discard the current record? [Y/N]:").lower()
            if data_confirm == "y":
                print("Data discarded.")
                break
            elif data_confirm == "n":
                updated_df = pd.concat([database, new_data], ignore_index=True)
                updated_df.to_csv(db_name, index=False)

        # User input: Ask if the user wants to add another song
        option = input("Do you still want to add another song [Y/N]: ").lower()
        if option != "y":
            delay()
            print("Thank you for using MixSync!")
            break