# Caprice Godinez
# Final Project: Make A Playlist

# This program simulates what it would be like for a user to create a music playlist

# Creates empty list for the playlist
class MusicPlaylist:
    def __init__(self):
        self.playlist = []

    def add_song(self, song_name):
        self.playlist.append(song_name)     # 1. Adds a song to a playlist
        return f'{song_name} added to the playlist.'

    def remove_song(self, song_name):
        if song_name in self.playlist:
            self.playlist.remove(song_name)     # 2. Removes a song from the playlist
            return f'{song_name} removed from the playlist.'
        else:
            return f'{song_name} not found in the playlist.'

# 3. Displays the playlist
    def display_playlist(self):
        print('Current Playlist:')
        for idx, song in enumerate(self.playlist, 1):
            print(f'{idx}. {song}')

# Plays a song from the playlist or displays an error message if there are no available songs
    def play_song(self):
        if not self.playlist:
            return 'Playlist is empty. Add some songs.'

        print('Playing song:')
        print(f'Now playing: {self.playlist[0]}')

    def run(self):
        while True:
            print("\nMenu:")
            print('1. Add a song to the playlist')
            print('2. Remove a song from the playlist')
            print('3. Display the current playlist')
            print('4. Play a song from the playlist')
            print('5. Exit')

            choice = input('Enter your choice from 1-5: ')

            try:
                choice = int(choice)
                if choice == 1:
                    song_name = input('Enter the name of the song to add: ')
                    print(self.add_song(song_name))

                elif choice == 2:
                    song_name = input('Enter the name of the song to remove: ')
                    print(self.remove_song(song_name))

                elif choice == 3:
                    self.display_playlist()

                elif choice == 4:
                    self.play_song()

                elif choice == 5:
                    print('Exiting program...')
                    break

                else:
                    print('Invalid choice. Please try again.')

            except ValueError:
                print('Invalid input. Please enter a number.')


if __name__ == '__main__':
    playlist_manager = MusicPlaylist()
    playlist_manager.run()
