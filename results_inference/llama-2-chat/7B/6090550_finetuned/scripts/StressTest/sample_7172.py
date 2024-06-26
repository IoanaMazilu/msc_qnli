# The hypothesis refers to the range of problems Andy solves, which is also mentioned in the premise
# However, the specific numbers in the hypothesis are different from the ones in the premise

if 70 <= x <= 125:
    # the hypothesis refers to the same range of numbers as the premise, but with different numbers
    label = "neutral"
elif 40 <= x <= 125:
    # the hypothesis refers to a different range of numbers, which contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values are outside the range of the premise, then it's an entailment
    label = "entailment"

print(label)
