raj_age_difference_premise = 3
raj_age_difference_hypothesis = 7
hema_age_difference_premise = -2
hema_age_difference_hypothesis = -2

# the hypothesis talks about the age differences between Raj, Ravi and Hema, referenced also in the premise
if raj_age_difference_hypothesis < raj_age_difference_premise:
    # check if the hypothesis value contradicts the estimate of 'raj_age_difference_premise'
    label = "contradiction"
elif hema_age_difference_hypothesis != hema_age_difference_premise:
    # check if the age difference between Hema and Ravi in the hypothesis contradicts the same difference reported in the premise
    label = "contradiction"
else:
    # the premise gives exact age differences
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
