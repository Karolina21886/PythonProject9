a
    if 0 <= score <= 49:
        return "Незадовільно"
    if 50 <= score <= 69:
        return "Задовільно"
    if 0 <= 70:
        return "Добре"
    if 0 <= 90:
        return "Відмінно"
    :
        return "Некоректне значення балів"

try:
    score = int(input("Введіть кількість балів (0-100): "))
    print(f"Ваша оцінка: {get_grade(score)}")
except ValueError:
    print("Будь ласка, введіть ціле число від 0 до 100.")