share_difference_premise = 200
share_difference_hypothesis = 400

# the hypothesis talks about the difference between Mani and Rani's share, which is also mentioned in the premise
if share_difference_hypothesis >= share_difference_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
