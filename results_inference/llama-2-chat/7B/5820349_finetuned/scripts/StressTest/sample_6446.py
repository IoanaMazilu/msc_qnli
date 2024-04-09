frank_age_difference_premise = 14
frank_age_difference_hypothesis = 54

# the hypothesis talks about the age difference between Frank and John, also mentioned in the premise
if frank_age_difference_hypothesis!= frank_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
