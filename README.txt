Instruction:
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Requirement files check
In the folder you will find:
A main python program call “ context_question_respond.py 
A testing context files that contain the context of the question 
A testing question files that contain the question correlated to the context
*importance note
You can also make your own context and question files too if you want but please make sure that the context and question are matching in the same index(line). 
(for example: (line 1 in context file )water is a substance that you can consume. (line 1 in question files) what is water ?)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Before we run the algorithm we gonna need to do a few thing: 
Please run this in the terminal first:

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Install dependency(Libraries): (note install these in order please)
—-----------------------------------------------------------------------------------
*this program uses: google and openai api. 
pip install beautifulsoup4   
pip install google
pip install openai
pip install openai==0.28
( if the other method didn't work, use this format: py -m pip install *name of the install*)
(example: py -m pip install google)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Running the program:

Now that you have install all the dependencies you can run the code in terminal by typing this:
Py context_question_respond.py question.txt context.txt 
(Or)
Python context_question_respond.py question.txt context.txt

After this, the program will prompt you the following line: 
>there are two mode for this program one is where you read the question files and the answers file [1], and one is a interactive users input method [2] please choose one:
enter the mode for this program [1] or [2]: you can either put [1] or [2] here 
>when a prompt  asks “please enter the mood for your AI response etc….” you can just leave this empty or you can enter how you want it to reponds back to you in the format as follow:you are a *enter something here* assistant
>when a prompt asks ”category etc……” in [2] mode: this is for the searching function to limit its search range to a more relevant subject.You can just leave this empty too if you want.  
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Running the program: [1] mode 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is a read file only mode where the program will take the two files that you just have input in the terminal in the previous step and read them. 
Once it done read the files, it will construct a dictionary where the context is map as key and question is map as values
The program will also ask the user to modify the mood of the ai, however if they don't want to, then they can just leave it as empty. 
The information will then get passed into the openai and google search function, one key values set at the time and print out the result.
*note this will run with a speedlimit of 14 second per run. 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Running the program: [2]mode
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is a user interactive system where the user will enter information that appearing in a prompt in real time 
That information will then get checked and pass into the function of openai and google search and it will return the result.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  Testing:
The program will look into the context and question files for testing, each line on both files is matched together to form a dictionary. Thing to note: both files operate on the assumption that each line is a set, so if you were to miss inputting the set format in the files, it will still run but the output will be weird.
(for example: line 1 context: a dog is a 4 legs animal, (lines 1-4 are filter values therefore the program will skip them) line 5 question: what is a cat ?) The program will pack them together in a set like this: [a dog is a 4 legs animal : what is a cat ?] and that is what it will be asked, which doesn't make sense so avoid it. 
To test the system: you just need to put a sentence in a context file, and the question files and make sure that the question and the context for it makes sense.
Other Things to test: this program will skip the line if the line in the files is empty and or contain a invalid sentence.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Testing files ( context.txt will contain 17 case)(question.txt will contain 16 case)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Here a first few line of each files
Context = 4 line
the dog jumps over the a house
>>>>>>>>>>>>>>test case contains 5 legal elements,and 12 illegal elements>>>>>>>>>>>>>>>>>>>>   	 
the cat has gone missing
-----------------------------------
Question = 4 line 
what did the dog jumps over ?
>>>>>>>>>>>>>>>>>>>>>>>test case contains 6 legal elements,and 10 illegal elements >>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<                     	 
what happend to the cat ?
5+5 equal to what ?

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Drawbacks
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-Because this program uses an outside source api for its function, it is necessary to slow the program down in order for it to be safely run without triggering a bot flag and rendering it useless, therefore this program will run very slow.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 Some information I read while making this program
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thank you to: 
google search information: geekforgeek  
https://www.geeksforgeeks.org/performing-google-search-using-python-code/

Openai function: wellsr
https://wellsr.com/python/building-a-python-question-answering-system-with-chatgpt/

Google search(extra information): 
https://python-googlesearch.readthedocs.io/en/latest/

Troubleshoots openai api:
https://community.openai.com/t/is-it-me-or-everyone-else-gpt-api-doesnt-work-any-more/494220/3
A really helpful demo of what you can do in chat gpt.
https://www.youtube.com/watch?v=pGOyw_M1mNE 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
small extra note: when you run the program for the first time it will create a files name ".google-cookie" in the same location as this program are located, and that is ok because these are the cookie from the search request. 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
				END
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
