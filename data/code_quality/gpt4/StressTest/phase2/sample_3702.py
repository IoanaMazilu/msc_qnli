john_age_premise = 38
john_age_hypothesis = 48
daughter_age_premise = 13
daughter_age_hypothesis = 13

# the hypothesis refers to the age of John and his daughter, mentioned also in the premise
if john_age_premise > john_age_hypothesis:
    # check if the age of John in the premise contradicts the hypothesis that John is less than 48 years old
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of the daughter in the hypothesis contradicts the age of the daughter in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
