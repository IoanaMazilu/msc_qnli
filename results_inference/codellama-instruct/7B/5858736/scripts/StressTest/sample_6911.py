roshan_age = 5
raj_age = 7
roshan_age_ratio = 3/4
raj_age_ratio = 3/4

# the hypothesis refers to the age of Roshan and Raj and their age ratio
if roshan_age <= raj_age:
    # check if the estimate of 'roshan_age' contradicts the age of Roshan in the premise
    label = "contradiction"
elif roshan_age_ratio!= raj_age_ratio:
    # check if the age ratio in the hypothesis contradicts the age ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
