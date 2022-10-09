list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]

list_territories_class = [GreenZoneIndex(city['territory_name'], city['territory_area'], city['green_zones']) for city in list_territories]

print(list_territories_class)