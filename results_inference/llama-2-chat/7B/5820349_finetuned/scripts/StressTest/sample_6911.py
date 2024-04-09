roshan_age_diff_premise = 5
raj_age_diff_premise = 3
roshan_age_diff_hypothesis = 2
raj_age_diff_hypothesis = 3

# the hypothesis talks about the age difference between Roshan and Raj, which is also mentioned in the premise
if raj_age_diff_hypothesis!= raj_age_diff_premise:
    # check if the age difference between Raj and Roshan in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
elif roshan_age_diff_hypothesis!= roshan_age_diff_premise:
    # check if the age difference between Roshan and Raj in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
