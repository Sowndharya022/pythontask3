from datetime import datetime
def write_current_timestamp_to_file():
    current_timestamp= datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    file_name='timestamp.txt'
    with open(file_name,'w')as file:
        file.write(f"current timestamp:{current_timestamp}")
print("timestamp is written")
write_current_timestamp_to_file()