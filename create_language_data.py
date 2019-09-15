import argparse

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


def print_sentence(sent, my_x, my_y):
    #Check length and write to file                                                                                                                                      
    if len(sent) > 99:

        my_x.write(sent[:100])
        my_x.write('\n')

        my_y.write(code)
        my_y.write('\n')

        return True

    return False


def load_files(mylangs, labeldata, xdata, ydata):

    with open(mylangs) as mylangs:
        languages = mylangs.readlines()

    with open(labeldata) as labeldata:
        labels = labeldata.readlines()
    with open(xdata) as xdata:
        sentences = xdata.readlines()
    with open(ydata) as ydata:
        langcodes = ydata.readlines()

    return languages, labels, sentences, langcodes

        

def parse_arguments(parser):

#Adds arguments from the command line to the parser                                                                                                                              

    #To read from
    parser.add_argument("mylangs", type=str, help="The file containing the selected languages")
    parser.add_argument("labeldata", type=str, help="The file contraining language metadata")    
    parser.add_argument("xdata", type=str, help="The file containing the training or test sentences.")
    parser.add_argument("ydata", type=str, help="The file containing the lang codes corresponding to each sentence")

    #To write to
    parser.add_argument("my_x", type=str, help="The file for the new traning or test sentences output")
    parser.add_argument("my_y", type=str, help="The file for the new lang codes output")

    return parser.parse_args()


if __name__ == "__main__":

    #Parses the arguments from the command line                                                                                                                                     
    args = parse_arguments(argparse.ArgumentParser(description="Preprocess training and test data."))

    #Load files
    languages, labels, sentences, langcodes = load_files(args.mylangs, args.labeldata, args.xdata, args.ydata)

    
    #Preprocess    

    with open(args.my_x, 'w') as my_x, open(args.my_y, 'w') as my_y:

        for lang in languages:
            lnr = 0
            sentences_written = 0
            print(lang.strip())

            #Get label code                                                                                                                                                         
            code = get_code(lang, labels)

            #For each line that has this label code...                                                                                                                              
            for line in langcodes:
                if line.strip() == code:

                    #Get the sentence for that line                                                                                                                                 
                    sent = sentences[lnr]
                    
                    #Check sentence and print to file                       
                    if print_sentence(sent, my_x, my_y):
                        sentences_written +=1

                lnr +=1

            #Print the number of sentences that went into the data                                                                                                              
            print(sentences_written)
            print('\n')
