#cli input:
#python3 dna.py databases/small.csv sequences/1.txt
#python3 dna.py databases/large.csv sequences/5.txt
import sys
with open(sys.argv[2]) as file:
    dna = file.readline().strip()
with open(sys.argv[1]) as file:
    strs = file.readline().strip().split(",")[1:]
    max_num_list = ''
    for s in strs:
        counter=1
        while(counter*s in dna):
            counter += 1
        max_num_list += ','+str(counter-1)
    while True:
        next_line = file.readline().strip()
        if max_num_list in next_line:
            print(next_line.split(',')[0])
            exit()
        elif next_line == '':
            print("No match")
            exit()