john_age_premise = 3
tom_age_premise = 5
john_age_hypothesis = 6

# the hypothesis refers to the age difference between John and Tom mentioned in the premise
if john_age_premise!= john_age_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
elif tom_age_premise!= tom_age_hypothesis:
    # check if the age of Tom in the hypothesis contradicts the age of Tom in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
