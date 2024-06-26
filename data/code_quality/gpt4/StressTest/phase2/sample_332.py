efficiency_premise = 25
efficiency_hypothesis = 25

# the hypothesis talks about the efficiency of Tanya compared to Sakshi, as mentioned in the premise
if efficiency_hypothesis <= efficiency_premise:
    # check if the efficiency percentage in the hypothesis contradicts the efficiency percentage in the premise
    label = "contradiction"
else:
    # the premise gives an exact efficiency percentage
    # any efficiency percentage greater than 'efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
