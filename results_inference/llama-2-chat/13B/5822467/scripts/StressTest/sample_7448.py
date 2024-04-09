rahul_age_premise = 26
rahul_age_hypothesis = 26
deepak_age_premise = 3 * 4:3 = 12
deepak_age_hypothesis = 2 * 3 = 6

# the hypothesis refers to the ratio between Rahul and Deepak, and their ages after 6 years
if rahul_age_hypothesis == rahul_age_premise and deepak_age_hypothesis == deepak_age_premise:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
elif rahul_age_hypothesis!= rahul_age_premise or deepak_age_hypothesis!= deepak_age_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio and ages, and the hypothesis values do not contradict the premise values
    label = "neutral"

print(label)
