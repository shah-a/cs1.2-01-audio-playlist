from Playlist import Playlist

playlist = Playlist()

while True:

  # Prints welcome message and options menu
  print('''

  Welcome to Playlist Maker 🎶  

  =====================================
  Options:
  1: View playlist
  2: To add a new track to playlist
  3: To remove a track from playlist
  4: To search for track in playlist
  5: Return the length of the playlist
  =====================================

  ''')

  # Prints welcome message and options menu
  user_selection = int(input('Enter one of the 5 options:  '))

  # Option 1: View playlist
  if user_selection == 1:
    playlist.print_tracks()


  # Option 2: To add a new track to playlist
  elif user_selection == 2:
    track_title = input('What track do you want to add? ')
    playlist.add_track(track_title)



  # Option 3: To remove a track from playlist
  elif user_selection == 3:
    track_title = input('What track do you want to remove? ')
    playlist.remove_track(track_title)


  # Option 4: To search for track in playlist
  elif user_selection == 4:

    track_title = input('Which track do you want to find? ')
    index = playlist.find_track(track_title)
    
    if index == -1:
      print(f"The track {track_title} is not in the set list.")
    else:
      print(f"The track {track_title} is track number {index+1}")


  # Option 5: Return the length of the playlist
  elif user_selection == 5:
    print(f"This set list has {playlist.length()} tracks.")

  # Message for invalid input
  else:
    print('That is not a valid option. Try again.\n')
