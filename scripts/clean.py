import csv
from parent import CSVLoader

class CleanCSV(CSVLoader):
    def __init__(self, csv_folder):
        super().__init__(csv_folder)

    def normalize_data(self):
        raw_tracks = self.load_all_csvs()
        track_row = []
        artist_set = set()
        track_artist_rows = []

        artist_id_map = {}
        artist_id_counter = 1
        track_id_counter = 1

        for row in raw_tracks:
            title = row['title'].strip()

            duration_str = row['duration (seconds)'].strip()
            if duration_str == '':
                print(f"Skipping track '{row['title']}' due to missing duration")
                continue

            duration = int(row['duration (seconds)'])
            track_id = track_id_counter
            track_id_counter += 1

            artists = [a.strip() for a in row['artist'].split(',')]

            for artist_name in artists:
                if artist_name not in artist_id_map:
                    artist_id_map[artist_name] = artist_id_counter
                    artist_id_counter += 1

                artist_id = artist_id_map[artist_name]
                track_artist_rows.append({'trackId': track_id, 'artistId': artist_id})
            
            track_row.append({
                'id': track_id,
                'title': title,
                'duration': duration
            })

        artist_rows = [{'id': id, 'name': name} for name, id in artist_id_map.items()]

        return track_row, artist_rows, track_artist_rows


    def save_clean_csv(self, filename, fieldnames, rows):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
