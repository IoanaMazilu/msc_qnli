exports_increase_percentage_premise = 12.8
exports_increase_percentage_hypothesis = 10.5

# the hypothesis talks about the percentage increase in US exports, which is also mentioned in the premise
if exports_increase_percentage_hypothesis != exports_increase_percentage_premise:
    # check if the percentage increase in US exports in the hypothesis contradicts the percentage increase in US exports from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
