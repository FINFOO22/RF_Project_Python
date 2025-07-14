list_ = [3, 5, 1, 17, 8, 4, 10, -1, 28, 13, 5, 3, 3, 4, 8, 16] # practising ordering list

rearranged_indexes = []
for i in range(len(list_)):
    
    # print(rearranged_indexes)
    if len(rearranged_indexes) == 0:
        rearranged_indexes += [i] 
        continue
    elif list_[i] <= list_[rearranged_indexes[0]]:
        rearranged_indexes = [i] + rearranged_indexes
        continue
    elif list_[i] >= list_[rearranged_indexes[-1]]:
        rearranged_indexes += [i]
        continue
    
    print(f'{list_[i]} is now going into the while loop')
    print(f'Here is the current list organised: {[list_[x] for x in rearranged_indexes]}')
    start = 0
    mid = int(len(rearranged_indexes)/2)
    end = len(rearranged_indexes)-1
    while True:
            if list_[i] == list_[rearranged_indexes[mid]]:
                 print(f'{list_[i]} is equal to {list_[rearranged_indexes[mid]]}')
                 split1 = rearranged_indexes[0:mid]
                 split2 = rearranged_indexes[mid:]
                 rearranged_indexes = split1 + [i] + split2
                 print([list_[x] for x in rearranged_indexes])
                 break
            elif list_[i] > list_[rearranged_indexes[mid]]:
                print(f'{list_[i]} is more than {list_[rearranged_indexes[mid]]}')
                if list_[i] <= list_[rearranged_indexes[mid+1]]:
                    print(f'{list_[i]} is less than or equal to {list_[rearranged_indexes[mid+1]]}')
                    split1 = rearranged_indexes[0:mid+1]
                    split2 = rearranged_indexes[mid+1:]
                    rearranged_indexes = split1 + [i] + split2
                    print([list_[x] for x in rearranged_indexes])
                    break
                else:
                    start = mid
                    if mid == int((start + end)/2):
                        mid = mid + 1
                        continue
                    else:
                        mid = int((start + end)/2)
                        continue
            elif list_[i] < list_[rearranged_indexes[mid]]:
                print(f'{list_[i]} is more than {list_[rearranged_indexes[mid]]}')
                if list_[i] >= list_[rearranged_indexes[mid-1]]:
                    print(f'{list_[i]} is more than or equal to {list_[rearranged_indexes[mid-1]]}')
                    split1 = rearranged_indexes[0:mid]
                    split2 = rearranged_indexes[mid:]
                    rearranged_indexes = split1 + [i] + split2
                    print([list_[x] for x in rearranged_indexes])
                    break
                else:
                    end = mid
                    if  mid == int((start+end)/2):
                        mid = mid - 1
                        continue
                    else:
                        mid = int((start+end)/2)
                        continue
print(rearranged_indexes)
print(f'{[list_[x] for x in rearranged_indexes]}')




list_2 = [3, 5, 1, 17, 8, 4, 10, -1, 28, 13, 5, 3, 3, 4, 8, 16]
rearranged_indexes_2 = sorted(range(len(list_2)), key=lambda i: list_2[i])

print(rearranged_indexes_2)
print([list_2[x] for x in rearranged_indexes_2])


