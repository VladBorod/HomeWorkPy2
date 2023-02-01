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

# Введение данных и переменных

watermelon_number = int(input('Введите количество арбузов: '))
watermelon_max = 0
watermelon_min = 3000000
watermelon_temp = 0

# Основной цикл по счетчику

while watermelon_number > 0:
    watermelon_weight = int(input('Введите вес арбуза по одному, через Enter! (вес арбуза не может превышать 3 млн!): '))
    watermelon_number -= 1
    # Проверка максимального-----
    if watermelon_weight > watermelon_max:
        watermelon_max = watermelon_weight
        # Дополнительная проверка на случай если первый арбуз наименьший-----
        if watermelon_min > watermelon_max:
            watermelon_min = watermelon_max
    # Проверка минимального----- 
    elif watermelon_weight < watermelon_min: 
        watermelon_min = watermelon_weight
        # Дополнительная проверка-----
        if watermelon_min > watermelon_max:
            watermelon_min = watermelon_max

# Вывод данных 
 
print(f'Арбуз для Ивана Васильевича - {watermelon_max}. Арбуз для тёщи - {watermelon_min}.')


