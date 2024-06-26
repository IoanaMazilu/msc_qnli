frank_age_difference_premise = 15
frank_age_difference_hypothesis = 15

# the hypothesis talks about the age difference between Frank and John, referenced also in the premise
if frank_age_difference_hypothesis < frank_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference stated in the premise
    label = "contradiction"
elif frank_age_difference_hypothesis > frank_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference stated in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the age difference reported in the premise, we can infer entailment
    label = "entailment"

print(label)
