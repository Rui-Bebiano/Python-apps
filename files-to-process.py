import os
import math

#Define here the root folder --------------
root_dir = os.getcwd()

# Output table header --------------
print("\n  "+53*"_"+"\n | Subject"+33*" "+"|   Files   |\n"+" |-"+40*"-"+"|"+11*"-"+"|")

#Inicialization of counter of the "To Process" folder containing files --------------
i=0

#Using function os.walk() to traverse the file system under root_dir looking for "To Process" folders  --------------
for dir_path, dir_names, file_names in os.walk(root_dir):
    
    # Actions to perform in case of a "To Process" folder --------------
    if ('To Process' in dir_names):
        to_process_dir = os.path.join(dir_path, 'To Process')
        subject = to_process_dir.rsplit("\\")[-2].replace("_"," ")
        num_files = len([f for f in os.listdir(to_process_dir) if os.path.isfile(os.path.join(to_process_dir, f))])
        # Actions to perform if the folder contains files --------------
        if num_files>0:
            # spacing between elements of output table --------------
            spaces1 = (37-len(subject))*" "
            spaces2 = (4-math.floor(math.log10(num_files)))*" "
            spaces3 = 2*" "
            # Prints the subject and nr of files on the table --------------
            print(" | ",subject,spaces1,"|",spaces2,num_files,spaces3,"|")
            i+=1

# Message in case of no files --------------
if i==0:
    print(" | No files to process! :)"+17*" "+"|"+6*" "+"-"+4*" "+"|")

# Output table's end --------------
print(" |"+41*"_"+"|"+11*"_"+"|\n")