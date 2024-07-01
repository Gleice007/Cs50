def main():
    # Solicita ao usuário que insira uma entrada
    input_str = input("Digite algo: ")

    # Substitui cada espaço por '...'
    replaced_str = input_str.replace(' ', '...')

    # Imprime a entrada com espaços substituídos por '...'
    print("A entrada com espaços substituídos por '...':")
    print(replaced_str)

if __name__ == "__main__":
    main()
