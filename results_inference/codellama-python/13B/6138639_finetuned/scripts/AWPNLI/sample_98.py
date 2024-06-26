students_premise = 14.0
seats_per_bus_premise = 2.0
buses_hypothesis = 7.0

# the hypothesis refers to the number of buses, which can be computed from the premise
# compute the number of buses needed in the premise
buses_premise = students_premise / seats_per_bus_premise
if buses_hypothesis!= buses_premise:
    # check if the number of buses in the hypothesis contradicts the number of buses from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)