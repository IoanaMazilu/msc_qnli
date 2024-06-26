ice_cream_flavors_premise = 3
ice_cream_flavors_hypothesis = 7

# the hypothesis refers to the number of ice cream flavors in Jerry's parlor, mentioned also in the premise
if ice_cream_flavors_premise >= ice_cream_flavors_hypothesis:
    # check if the premise value contradicts the estimate of less than 'ice_cream_flavors_hypothesis'
    label = "contradiction"
elif ice_cream_flavors_premise != ice_cream_flavors_hypothesis:
    # the hypothesis gives an upper estimate for the number of ice cream flavors
    # the number of flavors in the premise is less than this estimate, but it cannot be explicitly entailed from the hypothesis
    label = "neutral"
else:
    # if the premise value and estimates do not contradict the hypothesis ones, we can infer entailment
    label = "entailment"

print(label)
