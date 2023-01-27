# AWS-mock-test
Bonus task

This script starts by importing the json module. The script then defines a function load_json which takes the name of the JSON file as input and loads the JSON file using json.load() function, it opens the file and read the content and return the json object.

PLEASE NOTE THAT THE JSON FILE MUST BE IN THE SAME DIRECTORY/FOLDER

It also defines a function write_json(data) which takes the json object in the same filepath and name of the new file as input and writes the JSON file using json.dump() function, it opens the file and write the json object content in the file.

The script then defines a main function process_json which takes the path and name of the JSON file as input. It calls the load_json function, which loads the JSON file, and stores the result in the data (q here).
The function then prints the entire JSON file, prompt the user to enter a key whose value they want to print, print the value of the key, prompt the user to enter a new value for the key, update the value of the key in the data, print the modified JSON file, prompt the user to enter the path and name of the new file, calls the write_json(data) function, which writes the modified JSON file to the new file, and finally prints the message that the modified JSON file has been written to the new file.

At last, it prompts the user for the path and name of the JSON file, and calls the process_json function with the input path and file name.

Also a sample fruits.json was included here for testing
