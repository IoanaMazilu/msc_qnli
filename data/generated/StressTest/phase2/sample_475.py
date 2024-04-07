# Premise: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is less than 7/9 of that of Pyarelal.
# Hypothesis: Ashok and Pyarelal invested money together in a business and share a capital of Ashok is 1/9 of that of Pyarelal.
# Golden Label: neutral

ashok_share_premise = 7/9
ashok_share_hypothesis = 1/9

# the hypothesis talks about the share of investment of Ashok and Pyarelal in a business, referenced also in the premise
if ashok_share_hypothesis > ashok_share_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ashok_share_premise'
    label = "contradiction"
elif ashok_share_hypothesis == ashok_share_premise:
    # check if the share of Ashok in the hypothesis equals the share of Ashok in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the share of Ashok
    # any share of Ashok less than 'ashok_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

