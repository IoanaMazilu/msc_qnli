ashok_share_premise = 1/9
ashok_share_hypothesis = 3/9

# the hypothesis regards the share of the capital Ashok invested in a business, also mentioned in the premise
if ashok_share_hypothesis < ashok_share_premise:
    # check if the share of the capital Ashok invested, according to the hypothesis, contradicts the share mentioned in the premise
    label = "contradiction"
elif ashok_share_hypothesis > ashok_share_premise:
    # check if the share of the capital Ashok invested, according to the hypothesis, is greater than the share mentioned in the premise
    label = "contradiction"
else:
    # if the share of the capital Ashok invested, according to the hypothesis, matches exactly the one mentioned in the premise, we infer entailment
    label = "entailment"

print(label)
