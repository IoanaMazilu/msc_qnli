john_age_premise = 38
john_age_hypothesis = 88
daughter_age_premise = 13
daughter_age_hypothesis = 13

# the hypothesis refers to the ages of John and his daughter, mentioned in the premise
if john_age_premise != john_age_hypothesis:
    # check if the age of John in the hypothesis contradicts the age of John reported in the premise
    label = "contradiction"
elif daughter_age_premise != daughter_age_hypothesis:
    # check if the age of John's daughter in the hypothesis contradicts the age of John's daughter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
