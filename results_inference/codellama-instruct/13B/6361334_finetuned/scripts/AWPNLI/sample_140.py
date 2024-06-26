num_students_premise = 10.0
num_students_off_bus_premise = 3.0
num_students_left_bus_hypothesis = 7.0

# the hypothesis refers to the number of students left on the bus, which are also mentioned in the premise
# compute the total number of students on the bus from the premise
num_students_on_bus_premise = num_students_premise - num_students_off_bus_premise
if num_students_left_bus_hypothesis!= num_students_on_bus_premise:
    # check if the number of students left on the bus in the hypothesis contradicts the number of students on the bus from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)