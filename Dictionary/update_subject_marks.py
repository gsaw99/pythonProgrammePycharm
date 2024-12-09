marks = {}

x = int(input("Enter phy marks here:"))
marks.update({"phy": x})

x = int(input("Enter math marks here:"))
marks.update({"math": x})

x = int(input("Enter che marks here:"))
marks.update({"che": x})

print(marks)