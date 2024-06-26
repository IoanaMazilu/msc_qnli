num_students_premise = 14.0
num_seats_per_bus_premise = 2.0
num_buses_hypothesis = 7.0

# the hypothesis refers to the number of buses needed, which is also mentioned in the premise
# compute the total number of students and seats from the premise
total_students_premise = num_students_premise
total_seats_premise = num_buses_hypothesis * num_seats_per_bus_premise
if total_students_premise > total_seats_premise:
    # check if the number of students from the premise exceeds the number of seats on the buses
    label = "contradiction"
else:
    # if the number of students from the premise does not exceed the number of seats on the buses, we can infer entailment
    label = "entailment"

print(label)
