# the hypothesis refers to the age difference between John and Tom, referenced also in the premise
if 6!= 2:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
