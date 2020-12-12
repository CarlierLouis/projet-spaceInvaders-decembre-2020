def jouer_console():
    import keyboard
    import time

    tab = [["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]

    def aff(tab):
        print("\n" * 10)
        for i in range(len(tab)):
            print()
            for j in range(len(tab[i])):
                print(tab[i][j], end='')

    def dep_a(l, c, tab):
        tab[l][c] = "_"
        if l % 2 == 0:
            if c == 9:
                l = l + 1
            else:
                c = c + 1
            tab[l][c] = "A"
            return tab, l, c
        if l % 2 == 1:
            if c == 0:
                l = l + 1
            else:
                c = c - 1
            tab[l][c] = "A"
            return tab, l, c

    def dep(l, c, p, tab):
        if p == -1 and c == 0: return tab, l, c
        if p == 1 and c == 9: return tab, l, c
        tab[l][c] = "_"
        tab[l][c + p] = "J"
        return tab, l, c + p

    def tir(tab, l, c, tir_test):
        tab[l - 1][c] = 'I'
        tir_test = True
        return tab, tir_test, l - 1, c

    def dep_tir(tab, c, l, tir_test):
        if l - 1 == -1:
            tir_test = False
            tab[l][c] = '_'
            l = 0
            c = 0

        if tir_test == True:
            l = l - 1
            tab[l][c] = 'I'
            tab[l + 1][c] = '_'

        return tab, l, c, tir_test

    def fin(l_a, c_a, l_t, c_t, end_game, win):
        if l_a == 4: end_game = True
        if l_a == l_t and c_a == c_t:
            end_game = True
            win = True
        return end_game, win

    tir_test = False
    end_game = False
    win = False
    l_a = 0
    c_a = 0
    l = 4
    c = 4
    l_t = 0
    c_t = 0
    tab[l_a][c_a] = "A"
    tab[l][c] = "J"
    aff(tab)

    while end_game == False:

        if keyboard.is_pressed('left'):
            tab, l, c = dep(l, c, -1, tab)
            tab, l_a, c_a = dep_a(l_a, c_a, tab)
            tab, l_t, c_t, tir_test = dep_tir(tab, c_t, l_t, tir_test)
            aff(tab)
            end_game, win = fin(l_a, c_a, l_t, c_t, end_game, win)
            time.sleep(0.3)

        if keyboard.is_pressed('right'):
            tab, l, c = dep(l, c, 1, tab)
            tab, l_a, c_a = dep_a(l_a, c_a, tab)
            tab, l_t, c_t, tir_test = dep_tir(tab, c_t, l_t, tir_test)
            end_game, win = fin(l_a, c_a, l_t, c_t, end_game, win)
            aff(tab)
            time.sleep(0.3)

        if keyboard.is_pressed('space'):
            if tir_test == False:
                tab, tir_test, l_t, c_t = tir(tab, l, c, tir_test)
                tab, l_a, c_a = dep_a(l_a, c_a, tab)
                end_game, win = fin(l_a, c_a, l_t, c_t, end_game, win)
                aff(tab)
                time.sleep(0.5)

    if win == True:
        print('vous avez gagné')
    else:
        print('vous avez perdu')
