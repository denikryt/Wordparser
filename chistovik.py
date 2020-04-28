from itertools import product
import subprocess 
import random

number = str(random.randint(0,10))

commands = ['for ', 'in ', 'if ', 'pass ', 'def ', 'None ','return ', 'range', '(',')',
':', number + ' ', '    ', '\n', 'var_one ', 'var_two ', 'var_three ', 'print ', "'", "'", '= ']

slova2 = ['"""','\n', 'y = exec(x)','\n', 'print(y)','\n', 
'with open', """('combinations.txt', 'a') """, 'as f:',
'\n', '    ', 'f.write(x +',"""'""", '''\\''', 'n', """'""", ')', 
'\n', 'f.close()']

def pars():
    for L in range(0, len(commands)+1):
        for x, subset in enumerate(product(commands, repeat=L)):
            log = []
            log.append(x)
            log.append(L)
            k = open("prov.py", 'w')     

            slova1 = ['x = """']
            for qe in slova1:
                k.write(qe)

            for i in subset:
                k.write(i)
                log.append(i)

            for we in slova2:
                k.write(we)

            k.close()

            with open('log.txt', 'a') as f:
                f.write(str(log)+'\n')
            f.close()

            subprocess.call(["prov.py"], shell=True)


pars()