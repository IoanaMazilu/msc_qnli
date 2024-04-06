# Premise: 2 House Democrat, Rep. Steny Hoyer of Maryland, told reporters that GOP leaders should n't expect much support for their plan.
# Hypothesis: Number two Democrat in House tells Republicans not to expect much support from them.
# Golden Label: entailment

democrat_rank_premise = 2
democrat_rank_hypothesis = 2

# the hypothesis mentions the Democrat's rank which is also mentioned in the premise
if democrat_rank_hypothesis != democrat_rank_premise:
    # check if the Democrat's rank in the hypothesis contradicts the rank mentioned in the premise
    label = "contradiction"
else:
    # if the Democrat's rank in the hypothesis does not contradict the rank in the premise, we can infer entailment
    label = "entailment"

print(label)

