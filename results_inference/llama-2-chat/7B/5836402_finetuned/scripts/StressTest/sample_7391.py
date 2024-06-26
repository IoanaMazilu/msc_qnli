efficiency_premise = 10
efficiency_hypothesis = 10

# the hypothesis refers to the efficiency of Rosy compared to Mary mentioned in the premise
if efficiency_hypothesis > efficiency_premise:
    # check if the hypothesis value contradicts the premise value of Rosy being more efficient than Mary by more than 'efficiency_premise' percentage
    label = "contradiction"
elif efficiency_hypothesis <= efficiency_premise:
    # check if the hypothesis value is less than 'efficiency_premise' percentage, which is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is exactly 'efficiency_premise' percentage, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
