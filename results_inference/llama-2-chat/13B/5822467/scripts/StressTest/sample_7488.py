apples_premise = 360
apples_hypothesis = 460

# the hypothesis refers to the number of apples possessed by Anita
if apples_hypothesis < apples_premise:
    # the hypothesis value is less than the premise value, no contradiction
    label = "entailment"
else:
    # the premise value is a lower bound for the number of apples possessed by Anita
    # any number of apples less than or equal to 460 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
