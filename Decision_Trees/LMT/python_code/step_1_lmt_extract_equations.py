import os
import re

# Find all files in a directory with extension .txt
myDir = '/Users/chao/GoogleDrive/2017-08-10_lmt'

pathList = []
for file in os.listdir(myDir):
    if file.endswith("results.txt") and file.startswith("lmt_"):
        # print(os.path.splitext(file)[0])    #remove the .txt extension from file name
        filePath = os.path.join(myDir, os.path.splitext(file)[0])
        pathList.append(filePath)
        # print(filePath)
# print pathList

for fileName in pathList:
    with open(fileName + ".txt", 'r') as weka_results:
        num_leaves = 0
        equation_list = []
        start_recording = False
        for row in weka_results:
            if row.startswith('Number of Leaves'):
                num_leaves = int(row.split(':')[1])
                print 'Number fo leaves : ' + str(num_leaves)

            elif row.startswith('LM_'):
                leaf_node = int(row.split(':')[0][3:])
                equation = 'LM_' + str(leaf_node) + '_prob = '
                #print 'Leaf node is ' + str(leaf_node)

            elif row.startswith('Class 0 :'):
                start_recording = True

            elif start_recording and row.startswith('\n'):
                start_recording = False
                str_list = re.split('\[|\]', equation)
                #print 'str_list is ' + str(str_list)
                clean_equation = ''
                for i in range(0, len(str_list)):
                    curr_str = str_list[i]

                    if '=' in curr_str and i != 0:
                        curr_str_list = curr_str.split('=')
                        curr_str = '(' + curr_str_list[0] + ' == \'' + curr_str_list[1] + '\')'
                    if curr_str[-1:] != ' ':
                        curr_str += ' '
                    if curr_str[:1] == ' ':
                        curr_str = curr_str[1:]
                    clean_equation += curr_str
                #print clean_equation
                equation_list.append(clean_equation)

            elif start_recording:
                equation += row[:-1]

            elif row.startswith('Time taken to build model:'):
                break
        with open(  fileName + "_extracted.txt", 'wb') as output_file:
            for str_i in equation_list:
                output_file.write(str_i + '\n\n')

        #print str(equation_list)

