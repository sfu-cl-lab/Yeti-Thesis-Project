import os
import re

# Find all files in a directory with extension .txt
myDir = '/Users/chao/GoogleDrive/2017-08-10_m5p/cross_validation/'

pathList = []
for file in os.listdir(myDir):
    if file.endswith("results.txt"):
        # print(os.path.splitext(file)[0])    #remove the .txt extension from file name
        filePath = os.path.join(myDir, os.path.splitext(file)[0])
        pathList.append(filePath)
        print(filePath)
# print pathList

for fileName in pathList:
    with open(fileName + ".txt", 'r') as weka_results:
        num_leaves = 0
        equation_list = []
        start_recording = False
        for row in weka_results:

            if row.startswith('LM num:'):
                leaf_node = int(row.split(':')[1])
                equation = 'LM_' + str(leaf_node) + '_pred = '
                #print 'Leaf node is ' + str(leaf_node)

            elif row.startswith('sum_7yr_GP ='):
                start_recording = True

            elif start_recording and row.startswith('\n'):
                start_recording = False
                str_list = equation.split()
                #print 'str_list is ' + str(str_list)
                clean_equation = ''
                for i in range(0, len(str_list)):
                    curr_str = str_list[i]

                    if '=' in curr_str and i != 1:
                        #print curr_str
                        curr_str_list = re.split('=|,', curr_str)
                        #print str(curr_str_list)
                        curr_str = '('
                        for j in range(1, len(curr_str_list)):
                            curr_str += curr_str_list[0] + ' == \'' + curr_str_list[j] + '\' or '
                        curr_str = curr_str[:-4] + ')'
                        #print curr_str
                    if curr_str[-1:] != ' ':
                        curr_str += ' '
                    if curr_str[:1] == ' ':
                        curr_str = curr_str[1:]
                    clean_equation += curr_str
                print clean_equation
                equation_list.append(clean_equation)

            elif start_recording:
                equation += row[:-1]

            elif row.startswith('Number of Rules'):
                num_leaves = int(row.split(':')[1])
                print 'Number fo leaves : ' + str(num_leaves)

            elif row.startswith('Time taken to build model:'):
                break
        with open(fileName + "_extracted.txt", 'wb') as output_file:
            for str_i in equation_list:
                output_file.write(str_i + '\n\n')

        #print str(equation_list)

