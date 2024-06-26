people_premise = 5
people_hypothesis = 3

# the hypothesis mentions the number of people taken to hospitals, which is also mentioned in the premise
if people_hypothesis < people_premise:
    # check if the number of people in the hypothesis is less than the number of people in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis is not less than the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
