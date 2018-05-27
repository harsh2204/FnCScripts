import re

# A very barebones regex based parsing script for loncapa assignments that can then be used to study different scores and question patterns in the questionares.
# This may later be able to turn the entire course content into a searchable database. This script is not intented to be used to make any automated solvers.
# Currently this script is setup to extract the parameters of a given question. This feature does not work flawlessly as there are gimmicks in questions to be accounted for.


#Author Harsh Gupta

#Need more noise filtration.
#Gotta fix the scientific notation eg. 4.21e-3 being parsed as [4.21,-3.0]
#Possible fix -> /[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?/

#Something else not sure how, but needs to be fixed is stuff like tension 1 being parsed eventhough its useless for the solutions. This includes subscripts being parsed as numbers as well
def parseCapa(name):

    textFile = open(name, "r")
    contents = textFile.read()
    textFile.close()
    lines = contents.split("Show MetadataProvide my evaluation of this resource")
    last = lines.pop()
    last = last.split("Threaded")[0]
    lines.append(last)
    lines = lines[1::]
    for i in range(len(lines)):
        current = re.split(r'\W*(Tries)\W*\d\/\d\d',lines[i])
        lines[i] = current
    for i in range(len(lines)):
        #remove all the "Tries" -> x[:] = (value for value in x if value != "Tries")
        lines[i][:] = (value for value in lines[i] if value != "Tries")
        lines[i][:] = (value for value in lines[i] if value != "\t\n")
    #Fix the random question number in the bracket as the first character
    for question in lines:
        for i in range(len(question)):
            if(question[i][0:2]=="\n("):
                # print(question[i])
                temp = question[i].split(")",1)[1::]
                question[i]= "".join(temp)
    questions = []
    for question in lines:
        for sub in question:
            params = [float(s) for s in re.findall(r'-?\d+\.?\d*', sub)]
            if(len(params)!= 0):
                questions.append(params)
    #final list of all the values
    print("Finished parsing all ", len(lines), " questions.")
    return questions
    # print(lines)
