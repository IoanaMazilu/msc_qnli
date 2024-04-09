sreedhar_days_premise = 75
sreedhar_days_hypothesis = 25
sravan_share_premise = 100 - sreedhar_days_premise
sravan_share_hypothesis = 100 - sreedhar_days_hypothesis

# the hypothesis refers to the number of days Sreedhar alone can do the work
if sreedhar_days_hypothesis <= sreedhar_days_premise:
    # check if the estimate of'sreedhar_days_hypothesis' contradicts the number of days Sreedhar alone can do the work in the premise
    label = "contradiction"
elif sravan_share_hypothesis!= sravan_share_premise:
    # check if the number of days Sreedhar alone can do the work in the hypothesis contradicts the number of days Sreedhar alone can do the work reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
