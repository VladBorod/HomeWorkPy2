# Задача 1. Иван Васильевич пришел на рынок 
# и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой 
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

watermelon_number = int(input('Введите количество арбузов: '))
watermelon_max = 0
watermelon_min = 0
watermelon_temp = 0

while watermelon_number > 0:
    watermelon_weight = int(input('Введите вес арбузов: '))
    watermelon_number -= 1
    watermelon_temp = watermelon_weight
    if watermelon_weight > watermelon_temp:
        watermelon_max = watermelon_weight
    else:
        watermelon_min = watermelon_weight
        

    



        

    print('макс', watermelon_max, 'мин', watermelon_min, 'temp', watermelon_temp)