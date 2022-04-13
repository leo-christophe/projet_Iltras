import sys
import subprocess
import time
installed_packages = ([r.decode().split('==')[0] for r in subprocess.check_output([sys.executable, '-m', 'pip',
'freeze']).split()])

def check_package(package,T_package):
    for i in range(len(T_package)-1):
        if package == T_package[i]:
            return True
        else:
            pass
    return False

def install_package(package):
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    package])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip',
    'freeze'])



def main_setup():
    print("Installation des paquets nécéssaires...")
    time.sleep(2)
    nec_pack = ['colorama','keyboard']
    iteration_loading = False
    for necessary_packages in range(0,len(nec_pack)):

        if iteration_loading == True:
            print(f'Téléchargement des packages... {(necessary_packages/(len(nec_pack)))*100}%')
            print(nec_pack[necessary_packages])
        else:
            pass

        if check_package(nec_pack[necessary_packages],installed_packages) == False:
            iteration_loading = True
            install_package(nec_pack[necessary_packages])
        else:
            
            iteration_loading = False

    print("- - - > Tout est installé, bon jeu!")



