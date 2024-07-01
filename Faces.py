def convert(input_str):
    # Substitui :) por 🙂
    result = input_str.replace(":)", "🙂")
    # Substitui :( por 🙁
    result = result.replace(":(", "🙁")
    return result

def main():
    # Solicita ao usuário que insira uma entrada
    input_str = input("Digite algo: ")

    # Chama a função convert para processar a entrada
    converted_str = convert(input_str)

    # Imprime o resultado convertido
    print("Resultado convertido:")
    print(converted_str)

if __name__ == "__main__":
    main()
