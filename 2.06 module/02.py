count_country = int(input("Кол-во стран: "))
text_list = dict()

for i_country in range(count_country):
    print(f"{i_country + 1} страна: ", end = "")
    text = input("").split()
    text_list[text[0]] = text[1::]

for i_city in range(3):
    flag = False
    print(f"{i_city + 1} город: ", end = "")
    cities = input("")
    
    for country in text_list:
        for city in text_list[country]:
            if city == cities:
                print(f"Город {city} расположен в стране {country}.")
                flag = True

    if not flag:
        print(f"По городу {cities} данных нет.")