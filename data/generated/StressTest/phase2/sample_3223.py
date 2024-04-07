# Premise: less than 6200 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: 4200 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: neutral

total_share_premise = 6200
total_share_hypothesis = 4200

# the hypothesis refers to the total share among John, Jose, and Binoy mentioned in the premise
if total_share_hypothesis >= total_share_premise:
    # check if the value of 'total_share_hypothesis' contradicts the estimate of less than 'total_share_premise'
    label = "contradiction"
elif total_share_hypothesis < total_share_premise:
    # the premise gives only an estimate for the total share
    # any number of shares less than 'total_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

