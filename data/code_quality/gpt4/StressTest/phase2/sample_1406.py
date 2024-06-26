raj_age_diff_premise = 3
raj_age_diff_hypothesis = 1
hema_age_diff_premise = -2
hema_age_diff_hypothesis = -2

# the hypothesis talks about the age difference between Raj, Ravi and Hema, referenced also in the premise
if raj_age_diff_hypothesis != raj_age_diff_premise:
    # check if the age difference between Raj and Ravi in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
elif hema_age_diff_hypothesis != hema_age_diff_premise:
    # check if the age difference between Hema and Ravi in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
