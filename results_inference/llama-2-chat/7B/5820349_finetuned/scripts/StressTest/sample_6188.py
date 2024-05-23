fuchsia_premise = 16
fuchsia_hypothesis = 36

# the hypothesis refers to the amount of Fuchsia paint mentioned in the premise
if fuchsia_hypothesis!= fuchsia_premise:
    # check if the amount of Fuchsia paint in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)