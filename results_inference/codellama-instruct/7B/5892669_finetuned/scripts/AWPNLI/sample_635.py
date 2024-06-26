buses_premise = 8.0
total_students_premise = 45.0
students_per_bus_hypothesis = 3.1

# the hypothesis refers to the number of students per bus, which can be inferred from the premise
# compute the number of students per bus in the premise
students_per_bus_premise = total_students_premise / buses_premise
if students_per_bus_hypothesis!= students_per_bus_premise:
    # check if the number of students per bus in the hypothesis contradicts the number of students per bus from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)