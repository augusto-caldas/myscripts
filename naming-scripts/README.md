## order-from-file
How it works:<br>
Reads a text file with multiple lines like `S01E01 - episode name` then goes over the episodes with just name compare it to file and add the matching episode number.<br>
Example: `episode name.mkv` -> `S01E01 - episode name.mkv`

***
## remove-brackets
Remove all brackets and the content inside of it.<br>
Example: `movie <blue-ray>[2010](1080p).mkv` -> `movie.mkv`.

***
## rename-files-10
Rename files to `S<season>E0<counter>`.<br>
Example: `S01E01...S01E99.`
## rename-files-100
Rename files to `S<season>E00<counter>`.<br>
Example: `S01E001...S01E999`.

***
## rename-directory
Rename directory based on file name.<br>
Example: `movie/movie-a.mkv` -> `movie-a/movie-a.mkv`