def main():

    try:
        co = float(input('cateto oposto: '))
        ca = float(input('cateto adjacente: '))
        if co < 1 or ca < 1:
            raise ValueError

        hi = (co ** 2 + ca ** 2) ** (1 / 2)
        print('Hipotenusa é {:.2f}'.format(hi))
    except ValueError:
        print('catetos precisam ser numeros reais positivos maiores que 0')

    reexec = input('Deseja reexecutar: (s/n) ')

    if reexec == 's' or reexec == 'n':
        if reexec == 's':
            main()
    else:
        print('entrada deve ser s ou n\n')
        reexec = input('Deseja reexecutar: (s/n) ')


if __name__ == "__main__":
    main()
