sravan_share_premise = 75
sreedhar_alone_premise = 75
sravan_share_hypothesis = 0
sreedhar_alone_hypothesis = 75

# the hypothesis refers to the share of Sravan, which is not explicitly mentioned in the premise
if sravan_share_hypothesis > sreedhar_alone_hypothesis:
    # check if the estimate of Sravan's share contradicts the premise
    label = "contradiction"
elif sreedhar_alone_hypothesis <= sravan_share_premise:
    # check if the estimate of Sreedhar's work time contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
