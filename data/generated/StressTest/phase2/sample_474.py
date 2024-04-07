# Premise: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is 1/9 of that of Pyarelal.
# Hypothesis: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is less than 7/9 of that of Pyarelal.
# Golden Label: entailment

ashok_share_premise = 1/9
ashok_share_hypothesis = 7/9

# the hypothesis refers to the share of capital of Ashok and Pyarelal mentioned in the premise
if ashok_share_hypothesis > ashok_share_premise:
    # check if the estimate of 'ashok_share_hypothesis' contradicts the share of capital in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

