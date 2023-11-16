import os
import shutil
import json

source_folder = "./bz2r_en/"
dest_folder = "./bucket/stock/des/"
map_filters = "./des_maptype_filter.json"
game_types = json.load(open(map_filters, 'r'))
bz2_des_ext = ".des"

for filename in os.listdir(source_folder):
    print(f"Opening {filename} ...")
    if filename.endswith(bz2_des_ext):
        file_path = os.path.join(source_folder, filename)

        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            file.close()

        # <game mode abbrv.> : <string in .des (unsorted) file>
        for gm_key, gamemode_search in game_types.items():
            if first_line == gamemode_search:
                gm_folder = os.path.join(dest_folder, gm_key)
                if not os.path.exists(gm_folder):
                    os.makedirs(gm_folder)
                    print(f"Created {gm_folder}")
                shutil.move(file_path, os.path.join(gm_folder, filename))
                print(f"Moved {filename} to {gm_folder}")
                break
            else:
                print(f"Ignoring {gm_key}")
    else:
        print(f"Skipping {filename} ...")
