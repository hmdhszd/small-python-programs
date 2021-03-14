mycollection = [["element1 of matris 1","element2 of matris 1"], ["element1 of matris 2","element2 of matris 2"], [0,0]]

for i in range(len(mycollection)-1):
    for j in range(len(mycollection[i])):
        mycollection[i][j] = input("\n Please enter element {} of matris {} :".format(j+1,i+1))
        if j==0:
            mycollection[2][0] += int(mycollection[i][j])
        else:
            mycollection[2][1] += int(mycollection[i][j])
        
        print(mycollection)
