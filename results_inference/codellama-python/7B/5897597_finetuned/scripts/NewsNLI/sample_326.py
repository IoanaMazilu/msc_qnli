sailors_premise = 15
sailors_hypothesis = 15

# the hypothesis mentions the number of sailors hurt in the incident, which is also mentioned in the premise
if sailors_hypothesis!= sailors_premise:
    # check if the number of sailors hurt in the hypothesis contradicts the number of sailors hurt in the premise
    label = "contradiction"
else:
    # if the number of sailors hurt in the hypothesis does not contradict the number of sailors hurt in the premise, we can infer entailment
    label = "entailment"

print(label)
