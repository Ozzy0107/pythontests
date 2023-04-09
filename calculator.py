import keyboard
import sys

class Calc:

    def execOp(self):
        try:
            while True:

                opInp = input("Insira a operacao que deseja fazer:\n")

                if opInp == 'q':
                    print('Bye!')
                    break
                opParts = opInp.split()

                self.op = opParts[1]
                self.int1 = opParts[0]
                self.int2 = opParts[2]

                if self.op == "*" or self.op == "x":
                    result = float(self.int1) * float(self.int2)
                    print(f'{self.int1} * {self.int2} = ' + str(result))
                elif self.op == "/":
                    result = float(self.int1) / float(self.int2)
                    print(f'{self.int1} / {self.int2} = ' + str(result))
                elif self.op == "-":
                    result = float(self.int1) - float(self.int2)
                    print(f'{self.int1} - {self.int2} = ' + str(result))
                elif self.op == "+":
                    result = float(self.int1) + float(self.int2)
                    print(f'{self.int1} + {self.int2} = ' + str(result))
                else:
                    print("Insira uma operacao valida")
#        except KeyboardInterrupt as e:
        except KeyboardInterrupt as e:
            print(f'Exit {e}')
            sys.exit()


if __name__ == '__main__':

    calcobj = Calc()
    calcobj.execOp()