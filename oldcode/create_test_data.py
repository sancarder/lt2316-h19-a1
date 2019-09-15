def get_code(lang, labels):
    
    for line in labels:

        #Ignoring first line                                                                                                                                                         
        if line == labels[0]:
            pass
        else:
            l = line.split(';')
            if l[1].strip() == lang.strip():
                code = l[0]
                print(code)

    return code

    
with open('languages.txt') as mylangs:
    languages = mylangs.readlines()
    print(languages)

with open('data/labels.csv') as labeldata:
    labels = labeldata.readlines()
with open('data/y_test.txt') as ydata:
    langcodes = ydata.readlines()
with open('data/x_test.txt') as xdata:
    sentences = xdata.readlines()

#Opening file for writing
with open('my_x_test_data.txt', 'w') as my_x, open('my_y_test_data.txt', 'w') as my_y:
        
    for lang in languages:
        lnr = 0
        nr_of_sents = 0
        sentences_written = 0
        print(lang.strip())
            
        #Get label code
        code = get_code(lang, labels)


        #For each line that has this label code...
        for line in langcodes:
            if line.strip() == code:
                nr_of_sents +=1

                #Get the line number
                lang_line = lnr
                #print(lang_line)

                #Get the sentence
                sent = sentences[lnr]

                #Check length and write to file                                                                                                                                     
                if len(sent) > 99:

                    my_x.write(sent[:100])
                    my_x.write('\n')

                    my_y.write(code)
                    my_y.write('\n')
                    sentences_written +=1
                
            lnr +=1

        #Print the number of sentences that made it into the data
        print(sentences_written)
        print('\n')
