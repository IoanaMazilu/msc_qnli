combinations_premise = 55
combinations_hypothesis = 45

# the hypothesis refers to the number of possible combinations in which Michael is not selected, also mentioned in the premise
if combinations_hypothesis == combinations_premise:
    # check if the hypothesis value contradicts the number of combinations in the premise
    label = "contradiction"
elif combinations_hypothesis < combinations_premise:
    # check if the hypothesis value is less than the number of combinations reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
