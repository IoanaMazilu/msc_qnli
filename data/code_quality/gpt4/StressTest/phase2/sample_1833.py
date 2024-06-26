toys_purchased_premise = 20
toys_purchased_hypothesis = 10

# the hypothesis refers to the number of toys purchased by Sam mentioned in the premise
if toys_purchased_premise <= toys_purchased_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values don't contradict the premise ones, it can be inferred as an entailment
    label = "entailment"

print(label)
