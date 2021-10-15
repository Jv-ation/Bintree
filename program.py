# The intended data structure for each node will be [node_value, rnode_value, lnode_value]
#creates a list to be iterated through for comparisons
tree_list = [10, 15, 5, 20, 11, 1, 9, 7, 17, 13]
print(tree_list)

#declares an list which will be used as to store lists which show the data from each node
main_list = []

#initiates the main loop, this will iterate for the whole list
for i in range(len(tree_list)):
    new_node = tree_list[i]
    next_node = 0
    if len(main_list) < 1:
        #using "", "" to 'hold open' the list places for l&rnodes
        main_list.append([new_node, "", ""])
        print(main_list)
    else:
        #long loop until operation is completed
        while True:
            
            
            if main_list[next_node][1] == '' and main_list[next_node][2] == '':
                print("running first if")
                if int(main_list[next_node][0]) > new_node:
                    main_list[next_node][1] = new_node
                    new_cnode = [new_node, "", ""]
                    main_list.append(new_cnode)
                    print(main_list)
                
                elif int(main_list[next_node][0]) < new_node:
                    main_list[next_node][2] = new_node
                    new_cnode = [new_node, "", ""]
                    main_list.append(new_cnode)
                    print(main_list)
                break
            
            elif main_list[next_node][1] == '':
                print("running first elif")
                if int(main_list[next_node][0]) > new_node:
                    main_list[next_node][1] = new_node
                    new_cnode = [new_node, "", ""]
                    main_list.append(new_cnode)
                    print(main_list)
                    break
                else:
                    node_to_find = main_list[next_node][2]
                    for i in range(len(main_list)):
                        if main_list[i][0] == node_to_find:
                            next_node = i
                            break
                        else:
                            pass
            
            elif main_list[next_node][2] == '':
                print("running 2nd elif")
                if int(main_list[next_node][0]) < new_node:
                    main_list[next_node][2] = new_node
                    new_cnode = [new_node, "", ""]
                    main_list.append(new_cnode)
                    print(main_list)
                    break
                else:
                    node_to_find = main_list[next_node][1]
                    for i in range(len(main_list)):
                        if main_list[i][0] == node_to_find:
                            next_node = i
                            break
                        else:
                            pass
            
            else:
                if main_list[next_node][0] < new_node:
                    node_to_find = main_list[next_node][2]
                    for i in range(len(main_list)):
                        if main_list[i][0] == node_to_find:
                            next_node = i
                            break
                        else:
                            pass
                
                else:
                    node_to_find = main_list[next_node][1]
                    for i in range(len(main_list)):
                        if main_list[i][0] == node_to_find:
                            next_node = i
                            break
                        else:
                            pass

for i in range(len(main_list)):
    print(main_list[i])