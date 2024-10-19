Students_Data = {
"Student_1":{"name":"John Kennedy","Reg_No":"2019534001","Gender":"Male"}, 
"Student_2":{"name":"Lucy Gerald","Reg_No":"2019534002","Gender":"Female"},
"Student_3":{"name":"Joy Sullivan","Reg_No":"2019534003","Gender":"Female"},
"Student_4":{"name":"Oliver Twist","Reg_No":"2019534004","Gender":"Male"},
"Student_5":{"name":"Grace Ekanem","Reg_No":"2019534005","Gender":"Female"}}
for student, data in Students_Data.items():
    print(f"{data['name']} with Reg No {data['Reg_No']} is a {data['Gender']}.")

