# Premise: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is 1/9 of that of Pyarelal.
# Hypothesis: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is less than 6/9 of that of Pyarelal.
# Golden Label: entailment

ashok_share_premise = 1/9
ashok_share_hypothesis = 6/9

# the hypothesis refers to the share of Ashok mentioned in the premise
if ashok_share_premise > ashok_share_hypothesis:
    # check if the share of Ashok in the hypothesis contradicts the share of Ashok reported in the premise
    label = "contradiction"
elif ashok_share_premise < ashok_share_hypothesis:
    # check if the share of Ashok in the hypothesis is more than the share of Ashok reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

