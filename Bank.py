def main():
    saudaçao = input("Digite uma saudação").strip().lower()
    if saudaçao.startswith("ola"):
        print("$0")
    elif saudaçao.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()                