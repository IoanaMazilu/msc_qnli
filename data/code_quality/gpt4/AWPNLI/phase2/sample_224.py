buses_premise = 8.0
students_per_bus_premise = 45.0
total_students_hypothesis = 360.0

# the hypothesis refers to the total number of students, which is also mentioned in the premise
# compute the total number of students in the premise
total_students_premise = buses_premise * students_per_bus_premise
if total_students_hypothesis != total_students_premise:
    # check if the total number of students in the hypothesis contradicts the total number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)