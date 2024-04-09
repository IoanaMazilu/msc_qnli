bus_capacity_premise = 8.0
students_premise = 45.0
students_per_bus_hypothesis = 3.1

# compute the total number of buses needed to transport all students
num_buses_premise = int(students_premise / students_per_bus_hypothesis)

# check if the number of buses in the hypothesis contradicts the number of buses in the premise
if num_buses_premise!= int(students_per_bus_hypothesis * students_premise):
    label = "contradiction"
else:
    # if the number of buses in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
