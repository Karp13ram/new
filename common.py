import csv
import subprocess
import time
a = ['upcoming.py', 'past.py', 'ocular.py', 'systemic.py']
outputs = []
for script_name in a:
    try:
        print("running")
        command = ["python3", "/home/clustrex/Downloads/new/" + script_name]
        result = subprocess.run(command, capture_output=True, text=True)

        print("hello"+str(result))
        # stdout_output = result.stdout.decode()
        # print(stdout_output)
        if result.returncode == 0:
            output = result.stdout
            outputs.append(output)
            time.sleep(10)
        else:
            print(f"Error running script '{script_name}': {result.stder}")
    except Exception as e:
        print(f"Exception while processing script '{script_name}': {str(e)}")

file_path = 'new.csv'
with open(file_path, 'r', newline='') as csvfile:
    rows = list(csv.reader(csvfile))

for i, row in enumerate(rows):
    row_index = i + 1 
    if row_index < len(outputs):
        j=-4
        row[j]=outputs[row_index - 1]
        j+=1
    else:
        row[j]=""
with open(file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)

# import csv
# import subprocess
# import time

# a = ['upcoming.py', 'past.py', 'ocular.py', 'systemic.py']
# outputs = []

# # for script_name in a:
# #     try:
# #         print("Running")
# #         command = ["python3", "/home/clustrex/Downloads/new/" + script_name]
# #         result = subprocess.run(command, capture_output=True, text=True)
# #         if result.returncode == 0:
# #             output = result.stdout.strip()  # Remove leading/trailing whitespace
# #             outputs.append(output)
# #             time.sleep(10)
# #         else:
# #             print(f"Error running script '{script_name}': {result.stderr}")
# #     except Exception as e:
# #         print(f"Exception while processing script '{script_name}': {str(e)}")

# file_path = 'new.csv'
# with open(file_path, 'r', newline='') as csvfile:
#     rows = list(csv.reader(csvfile))
#     for script_name in a:
#             print("Running")
#             command = ["python3", "/home/clustrex/Downloads/new/" + script_name]
#             result = subprocess.run(command, capture_output=True, text=True)

# for i, row in enumerate(rows):
#     row_index = i + 1
#     if row_index <= len(outputs):
#         j = -4  # Start from the last column
#         row[j] = outputs[row_index - 1]
#         j=j+1
#     else:
#         row.append("")  # Add a new column with an empty string for each row

# with open(file_path, 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(rows)


# # def common(file_path):
# # 	with open(file_path, 'r', newline='') as csvfile:
# # 		rows = list(csv.reader(csvfile))
# # 	for row in rows[1:]:
# # 		a=row[-3].strip()
# # 		print(a)
# # 		# print(row)
# # 		command=["python3","/home/clustrex/Downloads/chc/"+a]
# # 		if a!=" " or a!="File Name":
# # 			result=subprocess.run(command,capture_output=True, text=True)
# # 			# print(result.value())
# # 			try:
# # 				print("result",result)
# # 				b=result.stdout  #.replace("'",'"')
# # 				print("stdout",b)
# # 				b = b.replace("'",'"')
# # 				b = json.loads(b)
# # 				# print(b)
# # 				row[-2]=b["status"]
# # 				row[-1]=b["message"]
# # 				print(row[-3])
# # 				print(row[-2])
# # 				# break
# # 				time.sleep(20)
# # 			except Exception as e:
# # 				print(e)
# # 				continue
# # 		else:
# # 			print("Skipped")

# # 		print("\n\n\n--------------------------------------------------------\n\n\n",row)

# # 		with open(file_path, 'w', newline='') as csvfile:
# # 			csvwriter = csv.writer(csvfile)
# # 			csvwriter.writerows(rows)