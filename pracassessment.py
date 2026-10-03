school_name = "MHK Academy"
total_marks = 300
pass_percentage = 50
subject_pass_marks = 40
 
students = {
    101: {"name": "  ali raza ",   "math": 78, "english": 65, "science": 82},
    102: {"name": "SARA KHAN",     "math": 92, "english": 88, "science": 95},
    103: {"name": "bilal ahmed  ", "math": 45, "english": 38, "science": 50},
    104: {"name": "hina sheikh",   "math": 60, "english": 72, "science": 55}
}

#task1
def clean_name(name):
    return name.strip() .title()

# task2
def make_email(name):
    return name.lower() .replace("" , ".") + "@mhk.com"

# task3
def calculate_total(m1, m2, m3):
    return m1+m2+m3

# task4
def calculate_percentage(total , out_of =300):
    return round(total / out_of *100 , 1)

# task5 
def get_grade(percentage):
    if percentage >=90 and percentage <=100:
        return "A grade"
    elif percentage >=80 and percentage <=90:
        return "B grade"
    elif percentage >=70 and percentage <=80:
        return "C grade"
    elif percentage >=60 and percentage <=70:
        return "D grade"
    else:
        return "invalid input"

# task6
def get_result(m1, m2, m3, percentage):
    if percentage >= pass_percentage and m1 >= subject_pass_marks and m2 >= subject_pass_marks and m3 >= subject_pass_marks:
       return "pass"
    else:
        "fail"

# task7

def find_student(roll):
    record = students.get(roll)
    if record is None:
        return "Record not found"
    else : return (f"{record['name']} : Grade {get_grade()}") 