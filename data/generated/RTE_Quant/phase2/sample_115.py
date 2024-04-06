# Premise: Mrs. Bush's approval ratings have remained very high, above 80 %, even as her husband's have recently dropped below 50%.
# Hypothesis: 80% approve of Mr. Bush.
# Golden Label: neutral

approval_rating_mrs_bush_premise = 80
approval_rating_mr_bush_premise = 50
approval_rating_mr_bush_hypothesis = 80

# the hypothesis talks about the approval rating of Mr. Bush, which is also mentioned in the premise
if approval_rating_mr_bush_hypothesis > approval_rating_mr_bush_premise:
    # check if the approval rating of Mr. Bush in the hypothesis contradicts the approval rating in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

