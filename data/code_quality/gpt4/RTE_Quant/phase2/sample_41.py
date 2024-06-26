lower_percentage_premise = 5
upper_percentage_premise = 10
lower_percentage_hypothesis = 5
upper_percentage_hypothesis = 10

# the hypothesis talks about the percentage of stolen art that is returned to the owners, which is also mentioned in the premise
if lower_percentage_hypothesis != lower_percentage_premise or upper_percentage_hypothesis != upper_percentage_premise:
    # check if the percentage values in the hypothesis contradict the percentage values in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
