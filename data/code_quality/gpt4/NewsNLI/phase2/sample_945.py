score_premise = 1
score_hypothesis = 1

# the hypothesis mentions the result of the match between Inter Milan and CSKA Moscow, which is also mentioned in the premise
if score_hypothesis != score_premise:
    # check if the match result in the hypothesis contradicts the match result mentioned in the premise
    label = "contradiction"
else:
    # if the match result from the hypothesis does not contradict the match result in the premise, we can infer entailment
    label = "entailment"

print(label)