import os

directory = r"insert route"

def remove_faces(directory, remove_str):  
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            new_lines = []
            for line in lines:
                if remove_str not in line:
                    new_lines.append(line)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)


remove_faces(directory, "face-image:")