from read_csv_to_dict import *
from random import randint
from multi_variable_tree_functions_23062025 import *



data = csv_to_dict('Fish.csv', simplify_names=True)
# print(data)


## Fixing Functions One at a time
# 23062025 - BOOTSTRAPPING
def bootstrap(data, no_times=1):
    #
    # print(data)
    no_trees = 20
    # this would be done usually via obtaining the uploaded datas keys OR column headings if the data s in pandas format
   
    indexes = [randint(0, (len(data[list(data.keys())[0]])-1)) for i in range(0, len(data[list(data.keys())[0]]))] # generated list of indexes
    unused_samples = [i if i not in indexes else None for i in range(0, len(data[list(data.keys())[0]]))]
    unused_samples = [x for x in unused_samples if x is not None]
    #print(unused_samples)
    #print(indexes)

    # here i have obtained a system that ranomdly selects, and NOTES which indexes werent used in the Bootstrap
    # Now, reconstruct the dictionary (bootstrap_data)
    #print(bootstrapped_data)
    bootstrapped_data = {}
    for i in list(data.keys()):
        value = data[i]
        list_ = []
        for x in indexes:
            real = value[x]
            list_ = list_ + [data[i][x]]
        bootstrapped_data[i] = list_

    #print(bootstrapped_data)
    return bootstrapped_data # REMEMBER --> need to retain the unused indexes to process that data too for validation!


# print(bootstrapped_data)

















def best_variable_ssr_calculation(dependent_variable, independent_variable, rearranged_indexes, categorical=False):
    if categorical: # 02072025
        pass # here i need to write code for separating categorical data and assessing the ssr


    tree = {}
    # Start of the SSR 
    # Find the smallest SUM of SQUARED RESIDUALS
    ssr_list = []

    index_splits_calculated = []

    skip = 0 # skip intermediary values
    
    for i in range(0, len(dependent_variable), 1): # this currently does not split the data properly
        # split the root, then calculate the SSR for all the dat points
        skip_to = len(independent_variable) - list(independent_variable[::-1]).index(independent_variable[i]) -  1
        
        if i < skip_to:
            continue


        if i == skip_to:
            # print('DONE')
            split_1 = dependent_variable[:i+1]
            split_2 = dependent_variable[i+1:]
            # calculate ssr based on the average of either split
            squared_resids_1 = [(x - (sum(split_1)/len(split_1)))**2 for x in split_1]
            squared_resids_2 = [(x - (sum(split_2)/len(split_2)))**2 for x in split_2]

            # add ssr together
            ssr = sum(squared_resids_1) + sum(squared_resids_2)
            ssr_list.append(ssr)
            
            index_splits_calculated.append(i)
        
        else:
            continue
            split_1 = dependent_variable[:i+1]
            split_2 = dependent_variable[i+1:]
            # calculate ssr based on the average of either split
            squared_resids_1 = [(x - (sum(split_1)/len(split_1)))**2 for x in split_1]
            squared_resids_2 = [(x - (sum(split_2)/len(split_2)))**2 for x in split_2]

            # add ssr together
            ssr = sum(squared_resids_1) + sum(squared_resids_2)
            ssr_list.append(ssr)

            skip = False
            index_splits_calculated.append(i)


    #print(len(ssr_list))# here the ssr_ should be calculated for ONLY the index_splits_chosen - 27062025
    #print(len(index_splits_calculated))
    #print(len(dependent_variable))
    #print(f'here is the ssr list {ssr_list}')
    # obtain index for largest value in ssr_list
    for i in range(0,len(ssr_list),1):
        if ssr_list[i] == min(ssr_list):
            index = i
    ssr_ = ssr_list[index]
    ssr_corr_index = index_splits_calculated[index]
    
    #print(f'here is the index: {index}')
    #print(independent_variable)
    #print(independent_variable[index])
    #print(independent_variable[index+1])
    # obtain the independent variable value that the sum of squared residuals is lowest
    try:
        average = (independent_variable[ssr_corr_index] + independent_variable[ssr_corr_index+1])/2
    except:
        average = independent_variable[ssr_corr_index]
    # going to make the dictionary (tree)
    #print(f'here is the average{average}')
    tree[average] = [[[float(x) for x in list(independent_variable[:ssr_corr_index+1])], 
                      dependent_variable[:ssr_corr_index+1]], 
                      [independent_variable[ssr_corr_index+1:], dependent_variable[ssr_corr_index+1:]]]
    split_rearranged_indexes = [[x for x in list(rearranged_indexes[:ssr_corr_index+1])], [x for x in list(rearranged_indexes[ssr_corr_index+1:])]]
    # Currently this code can produce the first split.
    return average, tree, ssr_, split_rearranged_indexes







## Now, have to order lists ascending to measure the ssrs (dependent variable in ascending order and the)
# compare the ssr for each variable.
# We will assume that dependent (biomarker) variable is the one that we will measure and look at sum squared residuals for each one and see which is the lowest
# practise with mgkg
def re_order(bootstrapped, ind_name, dep_name): 
    # ordered_data = bootstrapped
    dep_var = bootstrapped[dep_name] # ACKNOWLEDGE this needs to change for when practise data no longer used
    ind_var = bootstrapped[ind_name] # need to order values based on the ind variable
    indexes = [x for x in range(0, len(ind_var))]
    rearranged_indexes = []
    if isinstance(ind_var[0], str): # if independent variable is a string, likely a categorical variable. - genie index calculation required
        # assumption is that categorical is always string
        # however, probably works, because discrete data will be split correctly in the else: statement below
        categorical = True
        categorical_positions = {}
        for i in range(0,len(indexes)):
            # print(f'index:{i}')
            try:
                if i == 0 :
                    #print(0)
                    rearranged_indexes = rearranged_indexes + [indexes[i]]
                    categorical_positions[ind_var[i]] = 0
                    continue
                elif ind_var[i] == ind_var[rearranged_indexes[-1]]:
                    #print(1)
                    rearranged_indexes = rearranged_indexes + [indexes[i]]
                    # wont have to update position index, because this is at the 'end' of the index list?
                    continue
                elif ind_var[i] in [ind_var[x] for x in rearranged_indexes]:
                    #print(2)
                    if ind_var[i] in list(categorical_positions.keys()):
                        # need to do: 23062025
                        # update the position dict, where any categorical data the start position in the rearranged indexes is stored, 
                        # therefore inserting a rearranged index that is before these groups means the groups start positions have moved up by ONE
                        # if they are further up
                        #
                        order = list(categorical_positions.keys())
                        position = 0
                        while True:
                            if order[position] == ind_var[i]:
                                #print(f'first in dict list : {order[position]}')
                                #print(f'the item to add : {ind_var[i]}')
                                position_to_split = categorical_positions[order[position]]
                                
                                split_1 = rearranged_indexes[0:position_to_split]
                                
                                split_2 = rearranged_indexes[position_to_split:]

                                rearranged_indexes = split_1 + [i] + split_2
                                for iter in range(position, len(order), 1):
                                    categorical_positions[order[iter]] += 1
                                    # this updates the positions of where stuff is so dont have to iterate throught everything everytime
                                break
                            else:
                                position += 1
                elif ind_var[i] not in [ind_var[x] for x in rearranged_indexes]:
                    #print(3)
                    rearranged_indexes = rearranged_indexes + [indexes[i]] # surely could just put i
                    categorical_positions[ind_var[i]] = len(rearranged_indexes)-1
                    continue
            except: 
                print('did not work')
                print(rearranged_indexes)
                print([ind_var[x] for x in rearranged_indexes])
                print(categorical_positions)
                print(ind_var[i])
                print(position)
                split_1 = rearranged_indexes[0:position_to_split]
                split_2 = rearranged_indexes[position_to_split:]
                rearranged_indexes = split_1 + [i] + split_2
                quit() # Issue seems to be 
                # when a name appears that is already present in the list that section of the if statement fails
                pass
                               
    # now fix the rearranging of indexes here
    else:
        #23062025 -- fixed it
        # need to sort this out also
        # quit()
        # easy to understand
        rearranged_indexes = sorted(range(len(ind_var)), key=lambda i: ind_var[i]) # orders list and retains old index of unordered list 
        categorical = False
        # so can apply to the rest of the variable lists


    # print(rearranged_indexes)
    #print([ind_var[x] for x in rearranged_indexes])
    #print(rearranged_indexes)
   
    # print(categorical_positions) # this is for arranging categorical variables
    #return
    reorder_ind = [ind_var[x] for x in rearranged_indexes]
    #print(ind_name)
    #print(f'INDEPENDENT VAR {reorder_ind}')
    reorder_dep = [dep_var[x] for x in rearranged_indexes]
    #print(dep_name)
    #print(f'DEPENDENT VAR {reorder_dep}')
    return rearranged_indexes, reorder_dep, reorder_ind, categorical
    # FIXED 27062025



# logical order of stuff - 02072025



# Next - best_ind_var - 230620256
# this gives the starting root choice


def best_ind_var(bootstrapped, dep_name):
    names = list(bootstrapped.keys())
    root_choice = {}
    for n in names:
        if n == dep_name:
            pass
        else:
            rearranged_indexes, reorder_dep, reorder_ind, categorical = re_order(bootstrapped=bootstrapped, ind_name=n, dep_name=dep_name)
            if categorical:
                print(f'{n} is a categorical variable')
                continue
            else:
                print(f'{n} is a continuous or discrete variable')
            average, tree, ssr_, split_rearranged_indexes = best_variable_ssr_calculation(dependent_variable=reorder_dep, 
                                                                independent_variable=reorder_ind,
                                                                rearranged_indexes=rearranged_indexes,
                                                                categorical=categorical)
            root_choice[n] = [tree, split_rearranged_indexes, ssr_]
    return root_choice
# this looks generally functional

















bootstrapped_data = bootstrap(data=data)
#23062025
#The reorder script is off - reading the code it does not reorder correctly
#Try again =- FIXED
re_order(bootstrapped=bootstrapped_data, ind_name='ïSpecies', dep_name='Weight')


rearranged_indexes, reorder_dep, reorder_ind, categorical = re_order(bootstrapped=bootstrapped_data, ind_name='Width', dep_name='Weight')


average, tree, ssr_, split_rearranged_indexes = best_variable_ssr_calculation(dependent_variable=reorder_dep, independent_variable=reorder_ind, rearranged_indexes=rearranged_indexes, categorical=categorical)
# testing this function now - 27062025
# Think it works now (for continuous independent variables -- need to tweak for categorical variables)

#print(tree)
#print(split_rearranged_indexes)




# current dont have way to distinguish categorical data
root_choice = best_ind_var(bootstrapped=bootstrapped_data, dep_name='Weight')

# Next step - work on categorical data?
# in the ssr calculation.



print(root_choice)# this works
#dictionary where:
#key is the variable name
# value is a list 
# [0] is a dictionary of the independent value average between the split
# the value is the independent and dependent values less than that, and the inde and depe values greater than that value
# [1] is the rearranged indexes for these splits
# [2] is the ssr




# next need to work out ssr for categorical data   
#line 70ish there - 02072025





