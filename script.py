with open('./input.csv','r') as f:
    temp_file = f.read()

temp_file = temp_file.split('\n')

output = []
output.append(temp_file[0])
for line in temp_file[1:]:
    temp_line = line.split(',')
    if temp_line[3].startswith('i'):
        temp_line[3] = '+' + temp_line[3][1:]
    output.append(','.join(temp_line))

with open('./output.csv','w') as f:
    f.write('\n'.join(output))
