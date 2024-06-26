# Define variables for the premise
boys_14_premise = 80
boys_15_premise = 70
boys_13_premise = 50
boys_12_premise = 60

# Define variables for the hypothesis
boys_14_hypothesis = 20
boys_15_hypothesis = 70
boys_13_hypothesis = 50
boys_12_hypothesis = 60

# Check if the hypothesis values contradict the premise values
if boys_14_hypothesis <= boys_14_premise:
    label = "contradiction"
elif boys_15_hypothesis!= boys_15_premise:
    label = "contradiction"
elif boys_13_hypothesis!= boys_13_premise:
    label = "contradiction"
elif boys_12_hypothesis!= boys_12_premise:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
