# Design Justification — Music Streaming Platform

## 1. Main Design Decisions

Classes identified: User, Artist, Album, Song, Playlist.
User is the central actor who interacts with all features.

## 2. Responsibilities Distribution

- User: Creates playlists, follows artists, manages library
- Playlist: Manages its own list of songs
- Artist: Owns albums
- Album: Contains songs, belongs to one artist
- Song: Belongs to one album

## 3. Relationships and Multiplicities

- Artist to Album: 1 to 0..* (an artist can have many albums)
- Album to Song: 1 to 1..* (an album must have at least one song)
- User to Playlist: 1 to 0..* (a user can have many playlists)
- Playlist to Song: 0..* to 0..* (many songs in many playlists)
- User to Artist: 0..* to 0..* (a user can follow many artists)

## 4. Alternatives Considered

- Excluded streaming/playback behavior as specified
- Chose Association over Composition for Album to Song

## 5. Trade-offs

- No playback modeling: simpler design but no listening history
- Song belongs to one album: clear hierarchy but no singles modeling
- Playlist owned by User: clear ownership but no collaborative playlists

## 6. Possible Improvements

- Add Genre class for better categorization
- Add collaborative playlists
- Add listening history
