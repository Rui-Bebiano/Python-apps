I wrote this small python app to help our team in managing the data loading process of our data warehouse. 
The system's ETL ingests data from source files wich are regularly distributed by dozens of subject-specific folders named "To Process", that are scattered in a file system.
We often need to know which of those folders contains files (and how many), preferabily without having to traverse the file system manually...

This app does that task automatically, and outputs a table indicating the subject (i.e., the name of the  parent folder) and the number of files in each "To Process" folder.
You can adapt the code to suit your needs (by selecting the root directory, and changing the name "To Process" to the folder you're looking after).

I mae available 2 versions of the same code, one commented in english, other in my native Portuguese ("_PT").
