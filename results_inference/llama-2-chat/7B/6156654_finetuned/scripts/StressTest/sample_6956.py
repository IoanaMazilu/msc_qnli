average_shirts_premise = 40
average_shirts_hypothesis = 40

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, which is also mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
