average_shirts_premise = 40
average_shirts_hypothesis = 80

# the hypothesis refers to the average number of shirts each person has, which is also mentioned in the premise
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it is entailed by the premise
    label = "entailment"

print(label)
