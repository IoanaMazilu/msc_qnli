parents_premise = 38
parents_hypothesis = 88

# the hypothesis refers to the number of parents participating in the Smithville PTA, which is also mentioned in the premise
if parents_hypothesis > parents_premise:
    # check if the hypothesis value contradicts the number of parents in the premise
    label = "contradiction"
elif parents_hypothesis < parents_premise:
    # check if the number of parents in the hypothesis is less than the number of parents reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
