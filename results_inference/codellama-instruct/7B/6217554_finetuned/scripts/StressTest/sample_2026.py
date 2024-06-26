# the hypothesis refers to the age difference between John and Tom, referenced also in the premise
if 6!= 5 + 3:
    # check if the number of yrs back in the hypothesis contradicts the number of yrs back reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
