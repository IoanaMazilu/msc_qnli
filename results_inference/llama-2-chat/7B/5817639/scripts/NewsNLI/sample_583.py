hotels_premise = 0
hotels_hypothesis = 0

# the hypothesis mentions the number of beachfront hotels under $200 in California, which is not mentioned in the premise
if hotels_hypothesis!= 0:
    # check if the number of beachfront hotels in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
