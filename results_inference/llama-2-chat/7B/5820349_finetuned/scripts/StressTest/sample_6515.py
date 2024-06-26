john_age_past_premise = 3
tom_age_past_premise = 6
john_age_past_hypothesis = 3
tom_age_past_hypothesis = 2

# the hypothesis refers to the age relation between John and Tom at certain points in the past
if john_age_past_premise!= john_age_past_hypothesis:
    # check if the age relation between John and Tom in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif tom_age_past_premise!= tom_age_past_hypothesis:
    # check if the age of Tom in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the age relations in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
