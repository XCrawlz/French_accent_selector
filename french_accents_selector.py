try:
    from getkey import getkey
except ImportError as err:
    print(err)
    print("run make install to install dependencies")
    quit()

try:
    import pyperclip
except ImportError as err:
    print(err)
    print("run make install to install dependencies")
    quit()

import sys


class Accent_Selector:
    def __init__(self):
        pass

    def append_choice_to_clip(self, char: str) -> None:
        try:
            pyperclip.copy(char)
        except pyperclip.PyperclipException as err:
            print(err)

    def append_a_g(self) -> None:
        self.append_choice_to_clip("à")

    def append_e_a(self) -> None:
        self.append_choice_to_clip("é")

    def append_e_g(self) -> None:
        self.append_choice_to_clip("è")

    def append_u_g(self) -> None:
        self.append_choice_to_clip("ù")

    def append_c_c(self) -> None:
        self.append_choice_to_clip("ç")

    def append_a_t(self) -> None:
        self.append_choice_to_clip("ä")

    def append_e_t(self) -> None:
        self.append_choice_to_clip("ë")

    def append_i_t(self) -> None:
        self.append_choice_to_clip("ï")

    def append_u_t(self) -> None:
        self.append_choice_to_clip("ü")

    def append_o_t(self) -> None:
        self.append_choice_to_clip("ö")

    def append_y_t(self) -> None:
        self.append_choice_to_clip("ÿ")

    def append_u_cir(self) -> None:
        self.append_choice_to_clip("û")

    def append_a_cir(self) -> None:
        self.append_choice_to_clip("â")

    def append_e_cir(self) -> None:
        self.append_choice_to_clip("ê")

    def append_i_cir(self) -> None:
        self.append_choice_to_clip("î")

    def append_o_cir(self) -> None:
        self.append_choice_to_clip("ô")

    def append_oe(self) -> None:
        self.append_choice_to_clip("œ")

    def append_ae(self) -> None:
        self.append_choice_to_clip("æ")

    def append_a_g_M(self) -> None:
        self.append_choice_to_clip("À")

    def append_e_a_M(self) -> None:
        self.append_choice_to_clip("É")

    def append_e_g_M(self) -> None:
        self.append_choice_to_clip("È")

    def append_c_c_M(self) -> None:
        self.append_choice_to_clip("Ç")

    def append_u_g_M(self) -> None:
        self.append_choice_to_clip("Ù")

    def append_e_t_M(self) -> None:
        self.append_choice_to_clip("Ë")

    def append_a_t_M(self) -> None:
        self.append_choice_to_clip("Ä")

    def append_i_t_M(self) -> None:
        self.append_choice_to_clip("Ï")

    def append_o_t_M(self) -> None:
        self.append_choice_to_clip("Ö")

    def append_u_t_M(self) -> None:
        self.append_choice_to_clip("Ü")

    def append_y_t_M(self) -> None:
        self.append_choice_to_clip("Ÿ")

    def append_e_cir_M(self) -> None:
        self.append_choice_to_clip("Ê")

    def append_o_cir_M(self) -> None:
        self.append_choice_to_clip("Ô")

    def append_u_cir_M(self) -> None:
        self.append_choice_to_clip("Û")

    def append_i_cir_M(self) -> None:
        self.append_choice_to_clip("Î")

    def choose_trema(self, gui: bool = False) -> None:
        if gui is True:
            print("a = ä / e = ë / i = ï/ o = ö/ u = ü/ y = ÿ")
        choice = getkey()
        if choice == "a":
            self.append_a_t()
        elif choice == "A":
            self.append_a_t_M()
        elif choice == "e":
            self.append_e_t()
        elif choice == "E":
            self.append_e_t_M()
        elif choice == "i":
            self.append_i_t()
        elif choice == "I":
            self.append_i_t_M()
        elif choice == "o":
            self.append_o_t()
        elif choice == "O":
            self.append_o_t_M()
        elif choice == "u":
            self.append_u_t()
        elif choice == "U":
            self.append_u_t_M()
        elif choice == "y":
            self.append_y_t()
        elif choice == "Y":
            self.append_y_t_M()
        else:
            if gui is True:
                print("wrong choice")

    def choose_circon(self, gui: bool = False) -> None:
        if gui is True:
            print("e = ê / i = î / o = ô / u = û")
        choice = getkey()
        if choice == "e":
            self.append_e_cir()
        elif choice == "E":
            self.append_e_cir_M()
        elif choice == "i":
            self.append_i_cir()
        elif choice == "I":
            self.append_i_cir_M()
        elif choice == "o":
            self.append_o_cir()
        elif choice == "O":
            self.append_o_cir_M()
        elif choice == "u":
            self.append_u_cir()
        elif choice == "U":
            self.append_u_cir_M()
        else:
            if gui is True:
                print("wrong choice")

    def menu(self, gui: bool = False) -> None:
        if gui is True:
            print("2 = é / 7 = è / 9 = ç / 0 = à /",
                  "{ = tréma / [ = circonflexe / ; = ù / o = œ / a = æ")
        choice = getkey()
        if choice == "2":
            self.append_e_a()
        elif choice == "@":
            self.append_e_a_M()
        elif choice == "7":
            self.append_e_g()
        elif choice == "&":
            self.append_e_g_M()
        elif choice == "9":
            self.append_c_c()
        elif choice == "(":
            self.append_c_c_M()
        elif choice == "0":
            self.append_a_g()
        elif choice == ")":
            self.append_a_g_M()
        elif choice == ";":
            self.append_u_g()
        elif choice == ":":
            self.append_u_g_M()
        elif choice == "{":
            self.choose_trema(gui)
        elif choice == "[":
            self.choose_circon(gui)
        elif choice == "o":
            self.append_oe()
        elif choice == "a":
            self.append_ae()
        else:
            if gui is True:
                print("wrong choice")


if __name__ == "__main__":
    selector = Accent_Selector()
    if len(sys.argv) == 1:
        selector.menu()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--gui" or sys.argv[1] == "-g":
            selector.menu(True)
        else:
            print(f"Error wrong argument {sys.argv[1]}")
            print("Either launch the program with '-g'",
                  "'--gui' or without args")
    else:
        print("Error, too much arguments")
        print("Either launch the program with '-g', '--gui' or without args")
