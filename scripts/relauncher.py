import os, time

n = 0
while True:
    print ("\n" * 100)
    print('Relauncher: Launching...')
    mystring = '''  

░██████╗██████╗░░░░██╗░░░██╗██╗
██╔════╝██╔══██╗░░░██║░░░██║██║
╚█████╗░██║░░██║░░░██║░░░██║██║
░╚═══██╗██║░░██║░░░██║░░░██║██║
██████╔╝██████╔╝██╗╚██████╔╝██║
╚═════╝░╚═════╝░╚═╝░╚═════╝░╚═╝

Built on stability.ai - Designing and implementing solutions using 
collective intelligence and augmented technology

Credits: 
Stability AI team, Runway, huggingface, hlky, fromtheroot

'''

    print(mystring)
    if n > 0:
        print(f'\tRelaunch count: {n}')
    os.system("python scripts/webui.py")
    print('Relauncher: Process is ending. Relaunching in 0.5s...')
    n += 1
    time.sleep(0.5)
