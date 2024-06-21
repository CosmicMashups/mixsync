import pandas as pd
from match import delay


# Sort database by specified column
def sorting(database, db_name, sort_column):
    sort_order = input("Ascending or Descending? [A/D]: ")
    if sort_order.lower() == "a":
        sorted_df = database.sort_values(by=sort_column)
    elif sort_order.lower() == "d":
        sorted_df = database.sort_values(by=sort_column, ascending=False)
    sorted_df.to_csv(db_name, index=False)
    return sorted_df


def search_song(database, db_name, columns_to_display, div):
    avail_column = database.columns.values
    print(f"{div} SEARCH FIELDS {div}")
    for i in range(0, len(avail_column), 2):
        if avail_column[i]:  # Check if the current column is True
            if i + 1 < len(avail_column) and avail_column[i + 1]:  # Check if the next column exists and is True
                print("{:<15} {:<15}".format(f"[{i}] {avail_column[i]}", f"[{i + 1}] {avail_column[i + 1]}"))
            elif i + 1 >= len(avail_column) or not avail_column[i + 1]:  # Check if the next column does not exist or is not True
                print(f"[{i}] {avail_column[i]}")

    while True:
        search_field = int(input("Search by? [#]: "))
        if search_field in range(len(avail_column)):
            search_field = avail_column[search_field]
            search_term = input("Search Term: ").lower()
            sort_db = sorting(database, db_name, search_field)
            break
        else:
            print("Invalid specified column.")
            continue

    # Perform the search
    search_results = sort_db[sort_db[search_field].astype(str).str.contains(str(search_term), case=False, na=False)]

    # Display results
    delay()
    print(f"{div} SONGS {div}")
    print(search_results[columns_to_display])
    print(f"{div}======={div}")

    return search_results


# # User input: Ask if the list needs to be sorted
# sort_option = input("Do you want to sort the list (Yes/No): ").lower()
# if sort_option == "yes":
#     sort_column = input(f"How do you want to sort it ({', '.join(columns_to_display)}): ")
# else:
#     sort_db = database  # Use the unsorted database
