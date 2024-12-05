# Интепритатор записывает имя  файла в пременую __name__


print(1)


def main():
    print("__name__:", __name__)


if __name__ == "__main__":
    main()
