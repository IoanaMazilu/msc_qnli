initial_peanuts_premise = 4
additional_peanuts_premise = 12
initial_peanuts_hypothesis = 2
additional_peanuts_hypothesis = 12

# the hypothesis refers to the number of peanuts and the action of adding more peanuts in a box, as mentioned in the premise
if initial_peanuts_hypothesis != initial_peanuts_premise:
    # check if the initial number of peanuts in the hypothesis contradicts the number given in the premise
    label = "contradiction"
elif additional_peanuts_hypothesis != additional_peanuts_premise:
    # check if the number of additional peanuts in the hypothesis contradicts the number given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we have a neutral relation
    label = "neutral"

print(label)
