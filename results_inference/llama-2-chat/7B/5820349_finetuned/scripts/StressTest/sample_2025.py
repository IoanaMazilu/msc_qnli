john_age_multiple_premise = 3
john_age_multiple_hypothesis = 3
tom_age_back_premise = 6
tom_age_back_hypothesis = 5

# the hypothesis refers to the age relation between John and Tom mentioned in the premise
if john_age_multiple_hypothesis!= john_age_multiple_premise:
    # check if the multiple of John's age in the hypothesis contradicts the multiple in the premise
    label = "contradiction"
elif tom_age_back_hypothesis >= tom_age_back_premise:
    # check if the time back in the hypothesis contradicts the time back mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
