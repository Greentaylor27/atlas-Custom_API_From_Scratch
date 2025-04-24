from clean import CleanCSV

if __name__ == "__main__":
    cleaner = CleanCSV(csv_folder='CSVs')
    tracks, artists, track_artists = cleaner.normalize_data()

    cleaner.save_clean_csv('clean_tracks.csv', ['id', 'title', 'duration'], tracks)
    cleaner.save_clean_csv('clean_artists.csv', ['id', 'name'], artists)
    cleaner.save_clean_csv('clean_track_artists.csv', ['trackId', 'artistId'], track_artists)

    print("Clean CSVs created!")
