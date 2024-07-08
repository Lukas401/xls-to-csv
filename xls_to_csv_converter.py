import pandas as pd 
import os

def xls_to_csv(input_folder, output_folder):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".xls") or filename.endswith(".xlsx") or filename.endswith(".xlsm"):
            
            input_path = os.path.join(input_folder, filename)

            
            file_name_no_ext = os.path.splitext(filename)[0]

            
            output_path = os.path.join(output_folder, file_name_no_ext + ".csv")

            
            df = pd.read_excel(input_path)
            df.to_csv(output_path, index=False)

            print(f"Arquivo convertido: {output_path}")


input_folder = 'C:\\Users\\Tiadmin\\Documents\\Files XLS'
output_folder = 'C:\\Users\\Tiadmin\\Documents\\Files CSV'

xls_to_csv(input_folder, output_folder)
