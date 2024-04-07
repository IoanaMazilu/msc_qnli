# Premise: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is less than 3/9 of that of Pyarelal.
# Hypothesis: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is 1/9 of that of Pyarelal.
# Golden Label: neutral

ashok_share_premise = 3/9
ashok_share_hypothesis = 1/9

# the hypothesis refers to the share of Ashok in the business capital, which is also mentioned in the premise
if ashok_share_hypothesis > ashok_share_premise:
    # check if Ashok's share in the hypothesis contradicts the estimate of less than 'ashok_share_premise' in the premise
    label = "contradiction"
elif ashok_share_hypothesis < ashok_share_premise:
    # check if Ashok's share in the hypothesis is less than the 'ashok_share_premise'
    label = "entailment"
else:
    # if the Ashok's share in the hypothesis is equal to the 'ashok_share_premise'
    label = "neutral"

print(label)

