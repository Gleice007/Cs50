def camel_to_snake(name):
    result = [name[0].lower()]  # começamos com a primeira letra em minúsculo

    for char in name[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)

    return ''.join(result)

def main():
    camel_case_name = input("Digite o nome da variável em CamelCase: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print(f'O nome em Snake Case é: {snake_case_name}')

if __name__ == "__main__":
    main()
