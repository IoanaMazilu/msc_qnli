wounded_premise = 1000 # assuming "thousands" is a rough estimate
killed_premise = 1 # police officer and 5 demonstrators
killed_hypothesis = 6

# the hypothesis mentions the number of killed and wounded people, which are also mentioned in the premise
if killed_hypothesis < killed_premise:
    # check if the number of killed people in the hypothesis contradicts the number of killed people in the premise
    label = "contradiction"
elif killed_hypothesis > killed_premise:
    # check if the number of killed people in the hypothesis is greater than the number of killed people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
