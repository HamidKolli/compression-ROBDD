# Set the output to a png file
set terminal png size 500,500
# The file we'll write to
set output file_out
# The graphic title
set title titre
set xlabel sprintf("ROBDD node count for %s variables", nb_var)
set ylabel "Number of Boolean functions"
#plot the graphic
plot filename with lines