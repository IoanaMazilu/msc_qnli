exports_increase_premise = 12.8
exports_increase_hypothesis = 10.5

# the hypothesis talks about the increase in US exports, which is also mentioned in the premise
if exports_increase_hypothesis!= exports_increase_premise:
    # check if the increase in exports in the hypothesis contradicts the increase in exports from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
