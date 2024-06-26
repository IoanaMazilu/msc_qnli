john_age_difference_premise = 6
john_age_difference_hypothesis = 2

# the hypothesis talks about the age difference between John and Tom, referenced also in the premise
if john_age_difference_hypothesis!= john_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the age difference in the premise, we can infer entailment
    label = "entailment"

print(label)
