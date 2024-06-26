spending_premise = 17_000_000
spending_hypothesis = 17_000_000

# the hypothesis mentions the amount spent by Manchester City, which is also mentioned in the premise
if spending_hypothesis != spending_premise:
    # check if the spending in the hypothesis contradicts the spending reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
