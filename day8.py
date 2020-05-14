def checkStraightLine(coordinates):
            first=coordinates[0]
            second=coordinates[1]
            x1=first[0]
            y1=first[1]
            x2=second[0]
            y2=second[1]
            print("x1y1= ",x1,y1,"x2y2= ",x2,y2)
            slope=(y2-y1)/(x2-x1)
            
            for x in range(1,len(coordinates)-1):
                first=coordinates[x]
                second=coordinates[x+1]
                x1=first[0]
                y1=first[1]
                x2=second[0]
                y2=second[1]
                nSlope=(y2-y1)/(x2-x1)
                print("slope:",slope," new slope:",nSlope)
                if nSlope != slope:
                    return False
            return True
arr=[[0,1],[0,2],[0,3]]
print(checkStraightLine(arr))            
