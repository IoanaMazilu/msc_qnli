average_raise_premise = 2
average_raise_hypothesis = 7

# the hypothesis refers to the points Jerry wants to raise his average by, mentioned in the premise
if average_raise_hypothesis < average_raise_premise:
    # check if the hypothesis value contradicts the points Jerry wants to raise his average by in the premise
    label = "contradiction"
elif average_raise_hypothesis > average_raise_premise:
    # check if the hypothesis value is greater than the points Jerry wants to raise his average by in the premise
    label = "entailment"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
