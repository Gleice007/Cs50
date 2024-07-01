def convert_time_to_hours(time_str):
    # Convertendo o horário no formato HH:MM para um número de horas como float
    hour, minute = map(int, time_str.split(':'))
    return hour + minute / 60.0

def meal_time(hour_float):
    # Definição dos horários para cada refeição
    breakfast_start = 7.0
    breakfast_end = 9.0
    lunch_start = 12.0
    lunch_end = 14.0
    dinner_start = 19.0
    dinner_end = 21.0

    # Verificando em qual refeição o horário se encaixa
    if breakfast_start <= hour_float <= breakfast_end:
        return "breakfast time"
    elif lunch_start <= hour_float <= lunch_end:
        return "lunch time"
    elif dinner_start <= hour_float <= dinner_end:
        return "dinner time"
    else:
        return None  # Retorna None se não estiver em nenhum horário de refeição

def main():
    # Solicitando ao usuário que insira o horário
    time_str = input("Digite um horário no formato HH:MM (24 horas): ")

    try:
        # Convertendo o horário para um número de horas como float
        hour_float = convert_time_to_hours(time_str)

        # Verificando se o horário está dentro de algum horário de refeição
        result = meal_time(hour_float)

        # Imprimindo o resultado se estiver dentro de um horário de refeição
        if result:
            print(f"It's {result} now!")
        else:
            print("Não é hora de uma refeição.")

    except ValueError:
        print("Formato de horário inválido. Use o formato HH:MM.")

if __name__ == "__main__":
    main()
