share_premise = 4300
share_hypothesis = 1300

# the hypothesis talks about Deepak's share, which is also mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it is entailed
    label = "entailment"

print(label)
