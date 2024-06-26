bus_capacity_hypothesis = 3.1
total_students_premise = 45.0

# the hypothesis refers to the number of students per bus, which is not mentioned in the premise
# thus, no comparison can be made

# compute the number of buses needed for the premise
bus_needed_premise = total_students_premise / bus_capacity_hypothesis
if bus_needed_premise!= round(bus_needed_premise):
    # check if the number of buses from the hypothesis contradicts the estimate of buses needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
