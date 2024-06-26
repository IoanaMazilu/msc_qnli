efficiency_premise = 10
efficiency_hypothesis = 10

# the hypothesis talks about the efficiency of Rosy compared to Mary, referenced also in the premise
if efficiency_hypothesis >= efficiency_premise:
    # check if the hypothesis value contradicts the efficiency in the premise
    label = "contradiction"
elif efficiency_hypothesis < efficiency_premise:
    # if the hypothesis value is less than the efficiency in the premise, it is consistent with the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the efficiency in the premise, it is consistent with the premise
    # and can be explicitly entailed from the premise
    label = "entailment"

print(label)
