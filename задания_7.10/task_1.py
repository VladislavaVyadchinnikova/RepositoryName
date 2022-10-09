class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """
        # TODO все аргументы конструктора записать в атрибуты экземпляра класса
        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones

        self.green_index = None  # индекс озеленения
        # TODO посчитать индекс озеленения с помощью метода calculate_green_index
        self.calculate_green_index()

    def calculate_green_index(self):
        """
        Метод для вычисления индекса озеленения.

        Индекс рассчитывается как отношение площади всех парков к площади территории
        """
        all_area = 0
        for i in range(len(self.green_zones)):
          all_area += self.green_zones[i]
        self.green_index = all_area / self.territory_area
        
  
        # TODO посчитать индекс озеленения с атрибутов экземпляра класса


territory_name = "Пушкин"
territory_area = 28676
green_zones = [302, 487, 420, 325, 471, 363, 404]
# TODO Создать экземпряр класса и с помощью его атрибутов распечатать индекс озеленения в процентах до 2 знака после запятой. 
pushkin_city = GreenZoneIndex(territory_name, territory_area, green_zones)

print(f'Индекс озеленения территории {territory_name} равен {round(pushkin_city.green_index * 100, 2)}%')
# Ожидаемый ответ Индекс озеленения территории Пушкин равен 9.67%