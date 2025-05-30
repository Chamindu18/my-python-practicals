inputs = {
'input1' : "Hello world",
'input2' : 450000,
'input3' : 34.78,
'input4' : ("car","van","bus"),
'input5' : True,
'input6' : 1234567890,
'input7' : ['apple','banana','cherry'],
'input8' : {'name':'John','age':30}
}

for names,values in inputs.items():
    print(f"{names} : Data Type {type(values)}") 