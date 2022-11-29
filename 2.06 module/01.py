def music_times(time):
    result = 0
    for i_time in range(how_many):
        print("Название {0} песни: ".format(i_time + 1), end = "")
        name = input()
        result += violator_songs[name]
    return round(result, 2)

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

how_many = int(input("Сколько песен выбрать? "))
my_music_time = music_times(how_many)
print("Общее время звучания песен:", my_music_time)