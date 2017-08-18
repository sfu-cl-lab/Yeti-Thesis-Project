import os
import re

# Find all files in a directory with extension .txt
myDir = '/Users/chao/GoogleDrive/2017-08-17_m5p_TOI/cross_validation'

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
            if row.startswith('(using smoothed linear models)'):
                tree_found = True
            elif tree_found and row.startswith('LM num: 1'):
                tree_found = False
                list_len = len(branch_list)
                del branch_list[list_len - 1]
                del branch_list[0]
                list_len = len(branch_list)
                for i in range(0, list_len):
                    if "LM" in branch_list[i]:
                        leaf_pos_list.append(i)
                        leaf_mark_list.append(True)
                    else:
                        leaf_mark_list.append(False)

                # loop thru all leaves
                for j in range(0, len(leaf_pos_list)):
                    node_num = j + 1
                    leaf_pos = leaf_pos_list[j]
                    if leaf_pos == 0:
                        node_def = branch_list[0].split('LM')[0]
                    else:
                        node_def = ''
                        cond_list = []
                        # loop thru all branches from top to this leaf node
                        for pos in range(0, leaf_pos + 1):
                            if (not leaf_mark_list[pos] and pos != leaf_pos_list[j]) or pos == leaf_pos_list[j]:
                                print '\na. Looking at branch: ' + branch_list[pos]
                                curr_cond = (re.split('\>|\<', branch_list[pos]))[0]
                                print 'b: ' + curr_cond
                                #### Problem is here:
                                cond_replaced = False
                                for indx in range(0, len(cond_list)):
                                    if cond_list[indx].startswith(curr_cond):# and pos != leaf_pos_list[j]:
                                        print 'found:' + cond_list[indx]
                                        cond_list = cond_list[:indx]
                                        break
                                cond_list.append(branch_list[pos])

                        for indx in range(0, len(cond_list)):
                            temp_lst = cond_list[indx].split('|   ')
                            temp_lst = temp_lst[len(temp_lst) - 1].split(':')
                            cleaned_cond = temp_lst[0]

                            if 'Position' in cleaned_cond:
                                if '<' in cleaned_cond:
                                    temp_lst = re.split('\=|\<', cleaned_cond)
                                    cleaned_cond = temp_lst[0] + ' == ' + '\'' + temp_lst[1][0] + '\''
                                else:
                                    temp_lst = re.split('\=|\>', cleaned_cond)
                                    cleaned_cond = temp_lst[0] + ' != ' + '\'' + temp_lst[1][0] + '\''

                            if indx != len(cond_list) -1 :
                                cond_list[indx] = cleaned_cond + ' and '
                            else:
                                cond_list[indx] = cleaned_cond + ':'

                        for m in cond_list:
                            node_def = node_def + m

                    leaf_def_list.append(node_def)
                break
            elif tree_found:
                branch_list.append(row)

        #print "\nBranch list:\n"
        #for s in branch_list:
        #    print s
        #print 'Number of branches: ' + str(len(branch_list))
        #print '\n\nLeaf position list: ' + str(leaf_pos_list)
        #print '\n\nLeaf mark list: ' + str(leaf_mark_list)
        print '\n\nLeaf definition list:\n'
        for s in leaf_def_list:
            print s

    with open(fileName + ".txt", 'r') as weka_results:
        num_leaves = 0
        equation_list = []
        start_recording = False
        for row in weka_results:

            if row.startswith('LM num:'):
                leaf_node = int(row.split(':')[1])
                equation = 'm5p_pred = '
                #print 'Leaf node is ' + str(leaf_node)

            elif row.startswith('sum_7yr_TOI ='):
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
                #print clean_equation
                equation_list.append(clean_equation)

            elif start_recording:
                equation += row[:-1]

            elif row.startswith('Number of Rules'):
                num_leaves = int(row.split(':')[1])
                #print 'Number fo leaves : ' + str(num_leaves)

            elif row.startswith('Time taken to build model:'):
                break

    with open(fileName + "_extracted.txt", 'wb') as output_file:
        for leaf_i in range(0, num_leaves):
            leaf_str = """if %s\n    leafNode = %d\n    %s""" % (leaf_def_list[leaf_i], leaf_i + 1, equation_list[leaf_i])
            if leaf_i != 0:
                leaf_str = "el" + leaf_str
            output_file.write(leaf_str + '\n\n')

