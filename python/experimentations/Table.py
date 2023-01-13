
import os

def _init ():
    if(not os.path.exists("./experimentations/tab.md")) :
        with open(f"./experimentations/tab.md","a") as f:
            f.write("# Experimentation\n\n|No. variables |No. Samples |No. Unique Sizes  |Compute Time hh:mm:ss.ms |Seconds per ROBDD |\n|:------------:|:----------:|:----------------:|:--------------------:|:----------------:|\n")
            
def add_line_in_table(nombre_var,nbr_func,nbr_taille_differentes,temps,temps_par_robdd):
    _init()
    with open(f"./experimentations/tab.md","a") as f:
        f.write(f"|{nombre_var}  |{nbr_func}  |{nbr_taille_differentes} |{temps} |{temps_par_robdd}|\n")
