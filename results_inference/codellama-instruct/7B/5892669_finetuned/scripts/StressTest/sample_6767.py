people_premise = 13
people_hypothesis = 13

# the hypothesis refers to the number of people in a BCCI meeting mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the estimate of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
