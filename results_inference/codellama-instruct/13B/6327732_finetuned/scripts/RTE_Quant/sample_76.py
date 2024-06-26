hours_premise = 8
hours_hypothesis = 8

# the hypothesis talks about the number of hours for the demonstration and counter-demonstration, which are mentioned in the premise
if hours_hypothesis!= hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
