from termcolor import colored
from optparse import OptionParser
import os
from subprocess import call

parser = OptionParser()
parser.add_option("-v", action="store_true", dest="verbose", help="Show verbose output")
parser.add_option(
    "-c", 
    type=str, 
    dest="search_term", 
    help="Specify your own search term amongst running processes.", default=None)
(options, args) = parser.parse_args()

def verbose(data):
    if options.verbose:
        print(data)
        
def docker_ps_search_exec(search_term, command):
    stream = os.popen("docker ps")
    lines = stream.readlines()
    if len(lines) > 1:
        processes = []    
        for line in lines[1:]:
            elements = line.split()
            if search_term in elements[1] or search_term in elements[-1]:
                processes.append(line)

        if len(processes) == 0:
            print(colored("No docker processes matching {} found".format(search_term), "red"))
        elif len(processes) == 1:
            elements = processes[0].split()
            verbose(colored("Found one matching Docker process matching {}, connecting to {} ({})".
                format(search_term, elements[1], elements[-1]), 
                "green"))
            os.system("docker exec -t -i {} {}".format(elements[0], command))
        else:
            print(colored("Found multiple processes for {}".format(search_term), "yellow"))
            choice_string = ''         
            
            for index, process in enumerate(processes):
                elements = process.split()    
                choice_string = choice_string + "[{}]: {}\n".format(index+1, elements[-1])
                
            while True:
                try:
                    choice = input("Select one:\n[0]: Quit\n{}\n".format(choice_string))
                    if choice == 0:
                        break
                    elif choice - 1 < len(processes):
                        process = processes[int(choice) -1]
                        elements = process.split()
                        verbose(colored("Connecting to selected process to {} ({})".
                            format(elements[1], elements[-1]), 
                            "green"))
                        os.system("docker exec -t -i {} {}".format(elements[0], command))
                        break
                    else:
                        print(colored("Not a valid selection.\n", "red"))
                except NameError:
                    print(colored("Not a valid selection.\n", "red"))
    else:
        print(colored("No docker processes found", "red"))
        
def docker_bash():
    docker_ps_search_exec(options.search_term if options.search_term is not None else "_web", "bash")

def docker_psql():
    docker_ps_search_exec(options.search_term if options.search_term is not None else "postgres", "psql")
    


