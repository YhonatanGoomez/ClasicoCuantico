def RendiProb(Rendijas, Final):
    if (Final<=Rendijas):
        print("El número tiene que ser mayor que el número de rendijas")
    else:
        if (Final % Rendijas != 1):
            print("El número Final es inválido")
        else:
            fil=[]
            mat=[]
            for k in range(Rendijas+Final+1):
                for m in range(Rendijas+Final+1):
                    fil.append(0)
                mat.append(fil)
                fil=[]
            cont1=0
            for i in range(Rendijas+Final+1):
                for j in range(Rendijas+Final+1):
                    if i!=0:
                        if j==0:
                            if cont1<Rendijas:
                                mat[i][j]=1/Rendijas
                                cont1+=1
            pos=Final
            for x in range(1,Rendijas+Final+1,1):
                for y in range((Final//Rendijas)+1):
                    mat[pos][x] = 1/((Final//Rendijas)+1)
                    if y+1!=Final//Rendijas+1:
                        if pos+1==Rendijas+Final+1:
                            break
                        else:
                            pos+=1

            for r in range(Rendijas+Final+1):
                for l in range(Rendijas+Final+1):
                    if r>Rendijas+Final+1 or l>Rendijas:
                        if r==l:
                            mat[r][l]=1
                        else:
                            mat[r][l]=0
              
            return mat
                                
if __name__ == '__main__':
    print(RendiProb(2,3))


        
