import os
import re

# Find all files in a directory with extension .txt
myDir = '/Users/chao/GoogleDrive/2017-08-10_lmt/training_no_cv'

pathList = []
for file in os.listdir(myDir):
    if file.endswith("results.txt"):
        # print(os.path.splitext(file)[0])    #remove the .txt extension from file name
        filePath = os.path.join(myDir, os.path.splitext(file)[0])
        pathList.append(filePath)
        # print(filePath)
# print pathList

for fileName in pathList:
    with open(fileName + ".txt", 'r') as weka_results:
        branch_list = []
        leaf_pos_list = []
        leaf_def_list = []
        leaf_mark_list = []
        tree_found = False
        for row in weka_results:
            if row.startswith('------'):
                tree_found = True
            elif tree_found and row.startswith('Number of Leaves'):
                tree_found = False
                list_len = len(branch_list)
                del branch_list[list_len - 1]
                del branch_list[0]
                list_len = len(branch_list)
                for i in range(0, list_len):
                    if "LM_" in branch_list[i]:
                        leaf_pos_list.append(i)
                        leaf_mark_list.append(True)
                    else:
                        leaf_mark_list.append(False)

                for j in range(0, len(leaf_pos_list)):
                    node_num = j + 1
                    if leaf_pos_list[j] == 0:
                        node_def = branch_list[j].split('LM_')[0]
                    else:
                        node_def = ''
                        cond_list = []
                        last_cond = ''
                        for l in range(0, leaf_pos_list[j]):
                            if leaf_mark_list[l] == False:
                                curr_cond = (re.split('\>|\<', branch_list[l]))[0]
                                #print curr_cond
                                temp_lst = branch_list[l].split('|   ')
                                print temp_lst
                                cleaned_cond = temp_lst[len(temp_lst) - 1][:-1]
                                print cleaned_cond
                                if last_cond != curr_cond:
                                    cond_list.append(cleaned_cond + ' and ')
                                else:
                                    cond_list[len(cond_list) - 1] = cleaned_cond + ' and '
                                last_cond = curr_cond
                            else:
                                continue
                        temp_lst = branch_list[leaf_pos_list[j]].split('|   ')
                        temp_lst = temp_lst[len(temp_lst) - 1].split(': LM_')
                        cleaned_cond = temp_lst[0]
                        cond_list.append(cleaned_cond + ':')
                        for m in cond_list:
                            node_def = node_def + m
                    leaf_def_list.append(node_def)
                break
            elif tree_found:
                branch_list.append(row)

        print "\nBranch list:\n"
        for s in branch_list:
            print s
        print 'Number of branches: ' + str(len(branch_list))
        print '\n\nLeaf position list: ' + str(leaf_pos_list)
        print '\n\nLeaf mark list: ' + str(leaf_mark_list)
        print '\n\nLeaf definition list:\n'
        for s in leaf_def_list:
            print s

    with open(fileName + ".txt", 'r') as weka_results:
        num_leaves = 0
        equation_list = []
        tree_parsed = False
        start_recording = False
        for row in weka_results:
            if row.startswith('Number of Leaves'):
                num_leaves = int(row.split(':')[1])
                print 'Number fo leaves : ' + str(num_leaves)

            elif row.startswith('LM_'):
                leaf_node = int(row.split(':')[0][3:])
                equation = 'wx_sum = '
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

    with open(fileName + "_extracted.txt", 'wb') as output_file:
        for leaf_i in range(0, num_leaves):
            leaf_str = """if %s\n    leafNode = %d\n    %s\n    lmt_prob = 1/(1 + np.exp(wx_sum))""" % (leaf_def_list[leaf_i], leaf_i + 1, equation_list[leaf_i])
            if leaf_i != 0:
                leaf_str = "el" + leaf_str
            output_file.write(leaf_str + '\n\n')

