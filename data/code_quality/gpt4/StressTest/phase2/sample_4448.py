share_premise = 3000
share_hypothesis = 3000

# the hypothesis talks about the share of Christine, referenced also in the premise
if share_hypothesis > share_premise:
    # check if the hypothesis value contradicts the premise of being equal or less than 'share_premise'
    label = "contradiction"
elif share_hypothesis < share_premise:
    # if the hypothesis value is less than the premise, it can be explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it can be explicitly entailed from the premise
    label = "entailment"

print(label)
