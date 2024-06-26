people_premise = 15
people_hypothesis = 15

# the hypothesis refers to the number of people who entered the theater before Sujit mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the exact number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
