buses_premise = 8
buses_hypothesis = 4

# the hypothesis refers to the number of buses running between Chennai and Mysore mentioned in the premise
if buses_hypothesis >= buses_premise:
    # check if the number of buses in the hypothesis contradicts the estimate of less than 'buses_premise'
    label = "contradiction"
else:
    # any number of buses less than 'buses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
