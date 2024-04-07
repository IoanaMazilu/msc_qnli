# Premise: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is 1/9 of that of Pyarelal.
# Hypothesis: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is less than 4/9 of that of Pyarelal.
# Golden Label: entailment

ashok_share_premise = 1/9
ashok_share_hypothesis = 4/9

# the hypothesis refers to the share of Ashok in the business capital, also mentioned in the premise
if ashok_share_hypothesis > ashok_share_premise:
    # check if the share of Ashok in the hypothesis contradicts the share of Ashok reported in the premise
    label = "contradiction"
elif ashok_share_hypothesis == ashok_share_premise:
    # if the hypothesis value and estimate does not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only a number for Ashok's share
    # any share less than 'ashok_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

