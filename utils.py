import pandas as pd
import time

# Delay function for animation purposes
def delay():
    time.sleep(0.5)

# Read the database based on db_name
def read_database(db_name):
    if db_name.lower() == 'anime.csv':
        db_main = pd.read_csv(db_name)
        col_disp = ['BPM', 'TITLE', 'KEY', 'YEAR']
    elif db_name.lower() == 'western.csv':
        db_main = pd.read_csv(db_name)
        col_disp = ['ARTIST', 'TITLE', 'KEY', 'BPM']
    else:
        raise ValueError("Unsupported db_main name")

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    return db_main, col_disp


"""
# Check if input is numeric
def is_numeric(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False
"""

"""
# Sort database by specified column
def sorting(sort_column):
    sort_order = input("Ascending or Descending? [A/D]: ")
    if sort_order.lower() == "a":
        sorted_df = database.sort_values(by=sort_column)
    elif sort_order.lower() == "d":
        sorted_df = database.sort_values(by=sort_column, ascending=False)
    sorted_df.to_csv(db_name, index=False)
    return sorted_df
"""

# Find songs within specified BPM range
def bpm_finder(database, bpm, bpm_thresh):
    delay()
    print(f"Finding songs that are ±{bpm_thresh} BPM around {bpm} BPM...")
    bpm_min = bpm - bpm_thresh
    bpm_max = bpm + bpm_thresh
    find_bpm = database[(database['BPM'].between(bpm_min, bpm_max))]
    return find_bpm


# Find songs within specified key range
def key_finder(find_bpm, key, key_thresh, key_list):
    delay()
    print(f"Finding songs that are {key_thresh} keys apart from {key}...")
    key_index = key_list.index(key)
    surrounding_keys = []
    for counter in range(-key_thresh, key_thresh + 1):
        # if 0 <= key_index + counter < len(key_list):
        surrounding_keys.append(key_list[key_index + counter])
    find_keybpm = find_bpm[find_bpm['KEY'].isin(surrounding_keys)]
    return find_keybpm


# Function to generate sorted BPM values
def bpm_range(bpm, bpm_thresh):
    # Calculate the range of numbers around the midpoint
    start = bpm - bpm_thresh
    end = bpm + bpm_thresh

    # Generate the array of numbers within the range
    numbers = list(range(start, end + 1))

    # Sort the numbers based on their proximity to the midpoint
    numbers.sort(key=lambda x: abs(x - bpm))
    return numbers


# Function to create a custom sort order
def sort_bpm(df, midpoint, gap):
    sorted_bpm = bpm_range(midpoint, gap)
    sort_order = {bpm: index for index, bpm in enumerate(sorted_bpm)}
    df['sort_order'] = df['BPM'].map(sort_order)
    df = df.sort_values(by='sort_order').drop(columns=['sort_order'])
    return df


# Function to generate sorted keys based on proximity to the midpoint key
def key_range(key, key_thresh, key_list):
    midpoint_index = key_list.index(key)
    # Include the midpoint key first
    sorted_keys = [key]

    # Add keys within the gap range, alternating between lower and upper proximity
    for i in range(0, key_thresh + 1):
        lower_index = (midpoint_index - i) % len(key_list)
        upper_index = (midpoint_index + i) % len(key_list)

        sorted_keys.append(key_list[lower_index])
        sorted_keys.append(key_list[upper_index])

    # Filter out any duplicates while preserving order
    seen = set()
    sorted_keys = [mkey for mkey in sorted_keys if not (mkey in seen or seen.add(mkey))]

    return sorted_keys

# Function to create a custom sort order for the DataFrame
def sort_keys(df, key, key_thresh, key_list):
    sorted_keys = key_range(key, key_thresh, key_list)
    sort_order = {mkey: index for index, mkey in enumerate(sorted_keys)}
    print(sort_order)
    df.loc[:, 'sort_order'] = df['KEY'].map(sort_order)
    df = df.sort_values(by='sort_order').drop(columns=['sort_order'])
    return df