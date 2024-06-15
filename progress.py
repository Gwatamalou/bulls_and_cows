def intersections_number(key_number, user_number):
    """Сравнивает число игрока с загаданным числом
    """
    bull = 0
    cow = 0
    if key_number == user_number:
        return bull, cow, True
    for i in range(0, len(key_number)):
        for j in range(0, len(user_number)):
            if key_number[i] == user_number[j] and i == j:
                bull += 1
            elif key_number[i] == user_number[j]:
                cow +=1
    return bull, cow, False
