name = "aman"
math_marks = float(input("85: "))
science_marks = float(input("78:"))
english_marks = float(input("64:"))
total = math_marks + science_marks + english_marks
average = total/3

print("\n____result ____")
print("student:",name)
print("total marks:", total)
print("average marks:", average)

if average >= 40:
    print("result: pass")
else:
    print("result: fail")

marks = 78 
if marks >=90:
    print("grade:A")
elif marks >=75:
    print("grade:B")
elif marks >=40:
    print("pass")
else:
    print("fail")