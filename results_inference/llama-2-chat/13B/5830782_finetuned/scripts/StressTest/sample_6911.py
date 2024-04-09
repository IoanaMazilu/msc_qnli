roshan_age_diff_premise = 5
roshan_age_diff_hypothesis = 2

# the hypothesis talks about the age difference between Roshan and Raj, also mentioned in the premise
if roshan_age_diff_hypothesis!= roshan_age_diff_premise:
    # check if the age difference in the hypothesis contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # the hypothesis and premise agree on the age ratio
    label = "entailment"

print(label)
