min_abc_premise = min(2, 5, 7)
max_abc_premise = max(-7, -2, -3)
value_premise = max(min_abc_premise, max_abc_premise, 3)

min_abc_hypothesis = min(6, 5, 7) # The hypothesis gives a condition "less than 6" for one of the numbers, so in this case 6 is used
max_abc_hypothesis = max(-7, -2, -3)
value_hypothesis = max(min_abc_hypothesis, max_abc_hypothesis, 3)

# The hypothesis refers to the calculation of a value from a set of numbers, which is also mentioned in the premise
if value_hypothesis != value_premise:
    # check if the final value calculated in the hypothesis contradicts the value calculated in the premise
    label = "contradiction"
else:
    # if the value calculated in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
