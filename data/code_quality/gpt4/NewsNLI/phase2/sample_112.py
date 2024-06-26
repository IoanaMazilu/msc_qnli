passengers_premise = 150
passengers_hypothesis = 150

# the hypothesis mentions the number of passengers on the boat, which is also mentioned in the premise
if passengers_hypothesis != passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the number of passengers from the hypothesis does not contradict the number from the premise, we infer entailment
    label = "entailment"

print(label)
