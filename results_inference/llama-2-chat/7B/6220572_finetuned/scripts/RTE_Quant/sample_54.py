exports_growth_premise = 12.8
imports_growth_premise = 10.5
exports_hypothesis = 10.5

# the hypothesis talks about the growth of US exports, which is also mentioned in the premise
if exports_hypothesis!= exports_growth_premise:
    # check if the growth rate of exports in the hypothesis contradicts the growth rate of exports from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
