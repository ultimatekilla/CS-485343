# модуль призначено для роботи з зовнішніми файлами
# читання та виведення для візуального контролю

def get_indicators():
    """читання файла валюти `indicators`
    та формування списку валюти 
    повертає список валют
    """
    # накопичення даних файлу у списку 
    with open("./data/indicators.csv", 'r') as f:
         indicators = f.readlines()

    # підготовка даних для подальшої обробки
    indicators_splitted =[]
    # порізати в циклі строки на окремі елементи 
    for indicator in indicators:
       object = split_line(indicator)
       indicators_splitted.append(object)
            
    return indicators_splitted
    
def split_line(line):
    """повертає список обєктів з строки"""
    оbject = line.split(',')
    return object 



# модуль призначено для роботи з зовнішніми файлами
# читання та виведення для візуального контролю

def get_directorys():
    """читання файла валюти `indicators`
    та формування списку валюти 
    повертає список валют
    """
    # накопичення даних файлу у списку 
    with open("./data/directorys.csv", 'r') as f:
         directorys = f.readlines()

    # підготовка даних для подальшої обробки
    directorys_splitted =[]
    # порізати в циклі строки на окремі елементи 
    for directory in directorys:
       object = split_line(directory)
       directorys_splitted.append(object)
            
    return directorys_splitted

if __name__ == '__main__':
    indicators = get_indicators
    directorus = get_directorys 
    pass   