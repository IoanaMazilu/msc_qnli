num_students_premise = 14.0
num_seats_per_bus_premise = 2.0
num_buses_hypothesis = 7.0

# the hypothesis refers to the number of buses needed to take the trip, which is also mentioned in the premise
# compute the total number of students and seats from the premise
total_students_premise = num_students_premise * num_buses_hypothesis
total_seats_premise = num_seats_per_bus_premise * num_buses_hypothesis
if total_students_premise!= num_students_premise or total_seats_premise!= num_seats_per_bus_premise:
    # check if the number of students and seats from the hypothesis contradicts the number of students and seats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
