# Premise: Premier League champions Manchester City were the biggest spenders, splashing out nearly $17 million.
# Hypothesis: Manchester City are highest spenders after paying out $17 million.
# Golden Label: entailment

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

