MEDIUM_BLOCK = 50
LARGE_BLOCK = 100

def QuickFit(block_Size, blocks, process_Size, proccesses):

    allocate = [-1] * proccesses
    
    small_Blocks_List = []
    medium_Blocks_List = []
    large_Blocks_List = []

    for b in range(blocks): 
        if block_Size[b] < MEDIUM_BLOCK:
            small_Blocks_List.append(block_Size[b])
        elif (block_Size[b] < LARGE_BLOCK):
            medium_Blocks_List.append(block_Size[b])
        else:
            large_Blocks_List.append(block_Size[b])

    small_List_Len = len(small_Blocks_List)
    medium_List_Len = len(medium_Blocks_List)
    large_List_Len = len(large_Blocks_List)
    
    small_List_Occupied = [False] * small_List_Len
    medium_List_Occupied = [False] * medium_List_Len
    large_List_Occupied = [False] * large_List_Len
    
    for i in range(proccesses):
        if process_Size[i] < MEDIUM_BLOCK:
            for j in range(small_List_Len):
                if not small_List_Occupied[j] and (small_Blocks_List[j] >= process_Size[i]):
                    allocate[i] = j
                    small_List_Occupied[j] = True
                    break
        elif process_Size[i] < LARGE_BLOCK:
            for j in range(medium_List_Len):
                if not medium_List_Occupied[j] and (medium_Blocks_List[j] >= process_Size[i]):
                    allocate[i] = j
                    medium_List_Occupied[j] = True
                    break
        else:
            for j in range(large_List_Len):
                if not large_List_Occupied[j] and (large_Blocks_List[j] >= process_Size[i]):
                    allocate[i] = j
                    large_List_Occupied[j] = True
                    break

    print("Process No. Process Size Block No.")

    for i in range(proccesses):
        print(str(i + 1) + "\t\t\t" + str(process_Size[i]) + "\t\t\t", end=" ")

        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")


# Driver code

block_Size = [100, 50, 30, 120, 35]
process_Size = [20, 60, 70, 40]
m = len(block_Size)
n = len(process_Size)

QuickFit(block_Size, m, process_Size, n)