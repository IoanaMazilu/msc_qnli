frank_age_premise = 84
frank_age_hypothesis = 14
john_age_premise = 84
john_age_hypothesis = 14

# the hypothesis refers to the age difference between Frank and John
if frank_age_hypothesis <= frank_age_premise:
    # check if the estimate of 'frank_age_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
elif john_age_hypothesis!= john_age_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
