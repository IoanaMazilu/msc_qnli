people_premise = 13
people_hypothesis = 13

# the hypothesis refers to the number of people in a BCCI meeting mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"

print(label)
