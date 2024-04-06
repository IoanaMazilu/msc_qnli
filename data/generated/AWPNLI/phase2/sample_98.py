# Premise: The school is planning a field trip and there are 14.0 students and 2.0 seats on each school bus.
# Hypothesis: 7.0 buses are needed to take the trip.
# Golden Label: entailment

students_premise = 14.0
seats_per_bus_premise = 2.0
buses_needed_hypothesis = 7.0

# the hypothesis refers to the number of buses needed, which can be estimated from the premise
# compute the number of buses needed in the premise
buses_needed_premise = students_premise / seats_per_bus_premise
if buses_needed_hypothesis != buses_needed_premise:
    # check if the number of buses needed in the hypothesis contradicts the number of buses needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

