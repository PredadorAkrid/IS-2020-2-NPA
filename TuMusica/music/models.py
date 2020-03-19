from django.db import models

# Create your models here.
"""Music Models"""

def image_directory_path(instance, filename):
    """Get song directory path to save."""
    print(instance)
    return f"artists/images/{instance.id_artist}_{instance.name}_{filename}"

def song_directory_path(instance, filename):
    """Get song directory path to save."""
    print(instance)
    return f"music/songs/{instance.id_song}_{instance.name}_{filename}"

class Artist(models.Model):
    """Artist Model."""
    # campo nombre
    id_artist = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=image_directory_path, height_field=None, width_field=None, max_length=100)

    # Representación en cadena de un objeto artista
    def __str__(self):
        """Get str representation."""
        s = str(self.id_artist) + "" +  self.name
        return s
    def __repr__(self):
        """Get str representation."""
        return self.__str__()





class Song(models.Model):
    """Song Model."""
    id_song = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    song_file = models.FileField(null=True, upload_to=song_directory_path)

    # Relación muchos a muchos entre modelos song artist
    artists = models.ManyToManyField("music.Artist", related_name="songs")

    # Representación en cadena de un objeto song
    def __str__(self):
        """Get str representation."""
        artists_str = ""
        artists = list(self.artists.all())
        if len(artists) == 0:
            return f"{self.name}"
        artists_str = f"{artists[0].name}"
        for artist in artists[1:]:
            artists_str += f", {artist.name}"
        return f"{self.name} by {artists_str}"

    def __repr__(self):
        """Get str representation."""
        return self.__str__()