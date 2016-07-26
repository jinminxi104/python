import sys

if __name__=="__main__":
    print("main")
    for arg in sys.argv: 
        print arg
    print sys.argv[0]
    data = open(sys.argv[1])
    for each_line in data:
        print each_line
        line_elem = each_line.split(' ')
        print line_elem[0]
