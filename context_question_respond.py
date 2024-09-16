#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""context_answers system""" 
__author__="Toan Ngo"
#start file
import sys
import time
import openai               #this has being tested and it work 
openai.api_key = ["your api key here !"]
def google_search(user_input,category):             #the main search core is from geekforgeek, however the handle of data and it types are my code.
    try:                                #this use to check to make sure you have install google packet 
        from googlesearch import search
    except ImportError: 
        print("No module named 'google' found")   
    # to search
    #print(user_input)
    out_list=[]
    user_input=user_input.strip()
    category=category.strip()
    #conver_input=input("category: ")
    if (category=='') :
        category="General question" 
    combine=category+": "+user_input
    #print(combine)
    #langue=input("please enter the language en or es ").lower().strip()                    this modtify the language of the search 
    #print(langue)
    query = combine
    
    for j in search(query, tld="co.in",lang='en', num=2 , stop=3, pause=2.5):               #if i where to change the speed too fast google will block this !
        out_list.append(j)
    return out_list

def gpt(question,context,assistance_mode):                              #the main core of this is from wellsr of how you interact with ai, however i handle the data and the configuration of the ai. 
    message=[]                          #if you were to use this live version the chat will be able to remeber chat history because it read from the list, it also why we append the mode as the first thing in the code. 
    message=[{"role":"system","content":assistance_mode}]           #context for chat respond 
    combine_string= "here the context: "+ context + "." + "base on the context please answers this:" + question  
    if message:
        message.append({'role': 'user', 'content': combine_string},)
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=message,
                max_tokens=100,
                temperature=0.2,
                top_p=0.9)
    response_for_user=response['choices'][0]['message']['content']
    message.append({'role': 'user', 'content': response_for_user})
    return (f'The chat gpt respond is: {response_for_user}')
#------runner code-------------------------------------------------------------

user_question="".join(sys.argv[1])
user_context="".join(sys.argv[-1])
memory=[]
print("there are two mode for this program one is where you read the question files and the answers file [1], and one is a interactive users input method [2] please choose one: ")
while True:
        mode=input("enter the mode for this program [1] or [2]: ")
        mode=mode.strip()
        if mode=="[1]":
            memory.append(mode)
            break
        if mode=="[2]":
            memory.append(mode)
            break 
        else:
            print("please enter [1] or [2]") 
            continue

check_point=memory[0]
question_context_memory={}                              #format: context: question 
context_check=[]
question_check=[]
test2=True
#--------------mode[1] basic read file and work--------------------
if (check_point=="[1]"):
    #----------checking format----------------------------------------
    with open(user_context,'r')as inline_context:
        for line in inline_context.readlines():
            context_line=line.replace("\t","").replace("\n","").lower().strip()
            if context_line=="":
                continue
            elif (context_line[0] in ['"','"','-',''',''','—','_','>','<']) and (context_line[-1] in ['"','"','-',''',''','—','_','>','<']):
                continue
            else:
                context_check.append(context_line)                          #this will fill the list with the context of the files with the empty line this also give you a len
    #print(context_line)
    inline_context.close()
    with open(user_question,'r') as inline_question:
        for line in inline_question.readlines():
            question_line=line.replace("\t","").replace("\n","").lower().strip()
            if question_line=="":
                continue
            elif (question_line[0] in ['"','"','-',''',''','—','_','>','<','/']) and (question_line[-1] in ['"','"','-',''',''','—','_','>','<','/']):
                continue
            else:
                question_check.append(question_line)                        #this will fill the list of question 
    #print(question_line)                                                   #checker
    inline_question.close()                                                 #close the files they dont matter anymore 
    #------------------now two list have fill, check the len of both-----------------------------
    len_context=len(context_check)
    len_question=len(question_check)
    #print(len_context)                                                     #checker
    #print(len_question)                                                    #checker
    #print(question_check)                                                  #checker
    #print()                                                                    
    #print(context_check)                                                   #checker
    #print()   
    if len_context != len_question:                              #the context and question do not match 
        count=abs(len_context-len_question)
        #print(f'warning there are {count} missing context/ question in the files')
        if len_context > len_question:                           #the missing is on the question because there are more context than question.
            print(f'there are {count} missing in the question files.')
            for i in range(len_question):
                question_context_memory[context_check[i]]=question_check[i]                         #this should generate the dict
        else:                                                    #more question than context
            print(f'there are {count} missing in context files.')
            for i in range (len_context):
                question_context_memory[context_check[i]]=question_check[i]
    else:                                                        #both are equalt
        for i in range (len_context):
            question_context_memory[context_check[i]]=question_check[i]
    #----------------the dictionary should be populate with the context as key and question as values----------------------------------
    #--------------------------------------------------------------------------------------
    mood_of_ai=input("please enter the mood of your AI response, this will effect how it will respond.\n(examble:You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.) or you can leave this empty too if you like:(please press enter if you dont know/ dont want to enter anything.)\ninput: ").strip()
    #the code above will break if the user enter invalid string 
    #-----alternative solution------------------------------------
    #this will force the user to enter the correct string,however this will limited the users 
    '''while True:
        mood_of_ai=input("please enter something ").strip().split()
        if (mood_of_ai[0]== "you") and (mood_of_ai[1]=="are") and (mood_of_ai[-1]=="assistant") and (mood_of_ai[2]=="a") and (mood_of_ai[3] in ['kind','sassy','mean','annoying']) 
            break
        elif mood_of_ai=="":
            break
        else:
            print("please enter the follow format: you are a kind assistant ")
            continue
    '''
    #--------------empty mood check-----------------------------
    if mood_of_ai=="":
        mood_of_ai="you are a kind assistant"
    #-----------for testing--------------------
    #print(question_context_memory)
    #print(mood_of_ai)
    #print("done mode[1]")
    
    #------------------------------------------
    for key,values in question_context_memory.items():                  #dict context=key and question=values  this will run until the end is reach.
            print("-----------------------------------------------------------------------------------------------------")
            print("loading please wait !")
            openai_respond=gpt(values,key,mood_of_ai)               #gpt take (question,context,assistance_mode)
            print("searching the web.....")
            search_respond=google_search(values,'')                     #no category needed because it a files 
            #print(f'here some some more information for your question without the context \n {search_respond}')
            #print(f'this is the key ({key}) and this is the values({values})')
            print(f'{openai_respond} \nHere a are some more information for your question:\n {search_respond}')
            time.sleep(13)                                          #because limitation of the tool we have to slow our speed of input 
    print("-----------------------------------------------------------------------------------------------------")
    print("The program has done running !")
#---------------raw input mode[2]------------------------------
if (check_point=="[2]"):
    while True:
        raw_input_context=input("please enter your context for the question here: ").strip()
        raw_input_question=input("please enter your question here: ").strip()
        if (raw_input_context!="") and (raw_input_question!=""):
            break
        elif raw_input_question=="":
            print("please enter something for question !")
            continue
        elif raw_input_context=="":
            print("please enter something for the context !")
            continue
    category_of_question=input("please enter the category of the question here or you can leave this empty: ")
    openai_mood=input("please enter the mood of your AI response, this can change the way that it respond to you \n(for example:You are a poetic assistant, skilled in explaining complex programming concepts with creative flair. or you can just enter you are a poetic assistant without anything else) or you can left this empty too if you like:\n(please press enter if you dont know/ dont want to enter anything):")
    openai_mood=openai_mood.strip()                 #just in case of space
   #--testing mode[2] checker-----remove if need-----------
   # print("mode[2]")
   # print(raw_input_context)
   # print(raw_input_question)
   # print(category_of_question)
   # search_respond=google_search(raw_input_question,category_of_question)
   # print(f'here are some more information in related to your question \n {search_respond}')
    if openai_mood=="":
        print("loading please wait !")
        openai_mood="you are a kind assistant"
        openai_respond=gpt(raw_input_question,raw_input_context,openai_mood)
        print("searching the web......")
        search_respond=google_search(raw_input_question,category_of_question)
        print(f'{openai_respond} \nHere are some more information for your question:\n {search_respond}')
        print("The program has done running !")
    else:
        print("loading please wait !")
        openai_respond=gpt(raw_input_question,raw_input_context,openai_mood)
        print("searching the web.....")
        search_respond=google_search(raw_input_question,category_of_question)
        print(f'{openai_respond} \nHere are some more information for your question:\n {search_respond}')
        print("The program has done running !")
