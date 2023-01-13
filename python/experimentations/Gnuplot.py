from os import system

def plot(nombre_var):
    system(f"gnuplot -persist -e \"titre='Experimentation for {nombre_var} variables'\" -e \"nb_var='{nombre_var}'\" -e \"filename='./experimentations/gnuplot_data/nombre_var{nombre_var}.dat'\" -e \"file_out='./experimentations/gnuplot_diagrammes/nombre_var{nombre_var}.png'\" \"./experimentations/plot.plt\"") 

