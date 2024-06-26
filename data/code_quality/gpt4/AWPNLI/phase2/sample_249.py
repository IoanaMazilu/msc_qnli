elementary_schools_premise = 25.0
students_per_school_premise = 247.0
total_students_hypothesis = 6173.0

# The hypothesis refers to the total number of elementary students, which is a multiplication of the two numbers mentioned in the premise
total_students_premise = elementary_schools_premise * students_per_school_premise
if total_students_hypothesis != total_students_premise:
    # Check if the total number of students in the hypothesis contradicts the calculated total number of students from the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
