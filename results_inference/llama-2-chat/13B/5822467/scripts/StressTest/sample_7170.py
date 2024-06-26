problems_premise = 70
problems_hypothesis = 30

# the hypothesis refers to the range of problems solved by Andy in the premise
if problems_hypothesis <= problems_premise:
    # check if the hypothesis value contradicts the range of problems reported in the premise
    label = "contradiction"
elif problems_hypothesis > problems_premise:
    # check if the hypothesis value entails the range of problems reported in the premise
    label = "entailment"
else:
    # the premise gives only a range of problems, so any specific number greater than the range is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
