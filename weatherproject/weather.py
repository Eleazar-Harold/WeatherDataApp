
class Reader:
    def dataread(self, filename):
        if filename is None:
            exit()
        else:
            if filename.endswith('.dat'):
                f = open(filename)
                lines = f.readlines()[2:-1]
                return [data.strip().split() for data in lines]
                f.close()
            else:
                raise ValueError('Filename must end with .dat')

def main():
    arr = [] #empty array
    r = Reader() #instantiate Reader Class
    try:
        dt = r.dataread('weather.dat') #read weather.dat file using the dataread method in Reader Class
        index = 0
        for line in dt: #dt iteration to get targeted values from weather.dat file
            if index != 0 or index != len(dt)-1:
                dy = line[0] #assigns day to variable dy
                ln1 = line[1].split('*') #assumption: astericks was eliminated to use the integer value
                ln2 = line[2].split('*') #assumption: astericks was eliminated to use the integer value
                mxt = int(ln1[0]) #convert ln[1] string values to integer, assigns MXT value from weather.dat to variable mxt
                mnt = int(ln2[0]) #convert ln[2] string values to integer, assigns MNT value from weather.dat to variable mnt
                diff = (mxt-mnt) #get difference of [mxt] and [mnt] variables
                arr.append(diff) #append difference [diff] values to an array

            if diff == max(arr):
                print("{0} {1}".format(dy, diff)) # display of day and maximum spread
            index+=1
    except IOError as e:
        print("(Exception: ", e)
    except ValueError as e:
        print('Invalid file type: ', e)

if __name__ == '__main__': main()