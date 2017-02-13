
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
    arr = []  # empty array
    index = 0
    r = Reader()  # instantiate Reader Class
    try:
        dt = r.dataread('weather.dat')  # read weather.dat file using the dataread method in Reader Class
        for line in dt:  # dt iteration to get targeted values from weather.dat file
            dy = line[0]
            ln1 = line[1].split('*')  # assumption: asterisks was eliminated to use the integer value
            ln2 = line[2].split('*')  # assumption: asterisks was eliminated to use the integer value
            mxt = int(ln1[0])  # convert ln[1] string values to integer, assigns MXT value from weather.dat to variable mxt
            mnt = int(ln2[0])  # convert ln[2] string values to integer, assigns MNT value from weather.dat to variable mnt
            diff = (mxt - mnt)  # get difference of [mxt] and [mnt] variables
            if dy not in arr:
                arr.append([dy, diff])  # append difference [diff] values to an array

        for item in arr: #get each array item and iterate
            mxdiff = max(arr) #get array element with maximum difference
            set_dy = item[0] #append value to set_dy
            set_diff = item[1] #append value to set_diff
            if set_diff == mxdiff[1]: #equate the max difference(mxdiff) with each set_diff value
                #if the above statement is true the below print will be executed
                print("{0} {1}".format(set_dy, set_diff))  # display of day and maximum spread
                break

    except IOError as e:
        print("(Exception: ", e)
    except ValueError as e:
        print('Invalid file type: ', e)

if __name__ == '__main__': main()