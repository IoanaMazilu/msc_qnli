returned_tshirts_premise = 4
returned_tshirts_hypothesis = 8

# the hypothesis refers to the number of shirts Sanoop returned, which is also mentioned in the premise
if returned_tshirts_hypothesis < returned_tshirts_premise:
    # check if the hypothesis value contradicts the exact number of returned shirts reported in the premise
    label = "contradiction"
elif returned_tshirts_hypothesis > returned_tshirts_premise:
    # the premise gives an exact number of returned shirts
    # any number of returned shirts greater than 'returned_tshirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
