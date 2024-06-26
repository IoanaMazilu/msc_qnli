days_walked_premise = 3
days_walked_hypothesis = 8

# the hypothesis refers to the number of days Panjali walked, mentioned also in the premise
if days_walked_premise >= days_walked_hypothesis:
    # check if the number of days walked in the premise contradicts the hypothesis of 'less than days_walked_hypothesis'
    label = "contradiction"
elif days_walked_premise == days_walked_hypothesis - 1:
    # the premise explicitly states the number of days Panjali walked
    # if this number is exactly one less than 'days_walked_hypothesis', we can infer entailment
    label = "entailment"
else:
    # if the premise number of days walked is less than 'days_walked_hypothesis - 1', it is consistent with the hypothesis but cannot be explicitly entailed from it
    label = "neutral"

print(label)
