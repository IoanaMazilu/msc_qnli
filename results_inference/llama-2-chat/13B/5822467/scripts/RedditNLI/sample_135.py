quarter_premise = 2
quarter_hypothesis = 2

# the premise and hypothesis mention the number of quarters since a specific event

if quarter_hypothesis!= quarter_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters in the premise
    label = "contradiction"
elif quarter_hypothesis > quarter_premise:
    # check if the number of quarters in the hypothesis is greater than the number of quarters in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of quarters
    # any estimate of the number of quarters in the hypothesis greater or equal to the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
