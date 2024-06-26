people_entered_premise = 15
people_entered_hypothesis = 15

# the hypothesis refers to the number of people who entered the theater before Sujit, also mentioned in the premise
if people_entered_hypothesis <= people_entered_premise:
    # check if the hypothesis value contradicts the number of people who entered the theater in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
