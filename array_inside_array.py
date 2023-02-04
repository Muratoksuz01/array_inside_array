"""
def find_matrix(matrix, sub_matrix):
    for i in range(len(matrix) - len(sub_matrix) + 1):

        for j in range(len(matrix[i]) - len(sub_matrix[0]) + 1):

            if matrix[i][j:j+len(sub_matrix[0])] == sub_matrix[0]:

                for k in range(1, len(sub_matrix)):
                    if matrix[i+k][j:j+len(sub_matrix[k])] != sub_matrix[k]:
                        break
                else:
                    print("Sub-matrix found at position: (" + str(i) + ", " + str(j) + ")")
                    return
    print("Sub-matrix not found.")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
sub_matrix = [[5, 6], [8, 9]]
print(len(sub_matrix))
print(len(matrix))
find_matrix(matrix, sub_matrix)
"""
def dizibul(dizi,ara,bası=0):
    try:
        bas=dizi.index(ara[0],bası)
    except ValueError:
        print("listedee yok")
        exit()

        
    i=bas
    j=0
    son=bas
    while dizi[i]== ara[j]:
        if j!=len(ara):
            son+=1
            j+=1
            i+=1
        else:break



        print(f"baslangıc {bas} sonlan {son}")
        dizibul(dizi,ara,bas+1)





dizi=[1,2,3,4,5,3,4,5,6,3,4]
ara=[3,5]



dizibul(dizi,ara)

