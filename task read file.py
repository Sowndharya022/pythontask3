def write_to_file(file_name,content):
    with open(file_name,'w')as file:
        file.write(content)
    
file_name ='readfromfile.txt'
initial_content="hi its me sowndharya"

write_to_file(file_name,initial_content)

def read_from_file(file_name):
    with open(file_name,'r')as file:
        content=file.read()
    print(content)
file_name='readfromfile.txt'
print("reading to the content")

read_from_file(file_name)