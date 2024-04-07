# Premise: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is 1/9 of that of Pyarelal.
# Hypothesis: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is 3/9 of that of Pyarelal.
# Golden Label: contradiction

ashok_share_premise = 1/9
ashok_share_hypothesis = 3/9

# the hypothesis talks about the share of capital invested by Ashok and Pyarelal, which is also referenced in the premise
if ashok_share_premise != ashok_share_hypothesis:
    # check if the share of capital in the hypothesis contradicts the share of capital reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

