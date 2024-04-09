efficiency_premise = 35
efficiency_hypothesis = 25

# the hypothesis refers to the efficiency of Suresh compared to Kamal mentioned in the premise
if efficiency_hypothesis >= efficiency_premise:
    # check if the efficiency percentage in the hypothesis contradicts the efficiency percentage in the premise
    label = "contradiction"
elif efficiency_hypothesis < efficiency_premise:
    # if the efficiency percentage in the hypothesis is less than the efficiency percentage in the premise,
    # it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
