graduated_premise = 1
former_officer_premise = 1

# the hypothesis mentions the name and age of Tom Sponseller, which are also mentioned in the premise
if graduated_hypothesis!= graduated_premise:
    # check if the graduated status in the hypothesis contradicts the graduated status reported in the premise
    label = "contradiction"
elif former_officer_hypothesis!= former_officer_premise:
    # check if the former officer status in the hypothesis contradicts the former officer status in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
