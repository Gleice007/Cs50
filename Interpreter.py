# interpreter.py

def main():
    # Solicita ao usuário a expressão aritmética
    expression = input("Digite a expressão aritmética (no formato x y z): ")

    # Separa a expressão nos componentes x, y e z
    x_str, y_str, z_str = expression.split()

    # Converte x e z para inteiros
    x = int(x_str)
    z = int(z_str)

    # Determina o operador y e realiza o cálculo correspondente
    if y_str == '+':
        result = x + z
    elif y_str == '-':
        result = x - z
    elif y_str == '*':
        result = x * z
    elif y_str == '/':
        result = x / z

    # Imprime o resultado formatado com uma casa decimal
    print(f"O resultado da expressão {x} {y_str} {z} é: {result:.1f}")

if __name__ == "__main__":
    main()
