students_premise = 14.0
seats_per_bus_premise = 2.0
buses_hypothesis = 4.0

# the hypothesis refers to the number of buses needed, which is also mentioned in the premise
# compute the total number of buses needed in the premise
total_buses_premise = students_premise / seats_per_bus_premise
if buses_hypothesis != total_buses_premise:
    # check if the number of buses in the hypothesis contradicts the number of buses from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
