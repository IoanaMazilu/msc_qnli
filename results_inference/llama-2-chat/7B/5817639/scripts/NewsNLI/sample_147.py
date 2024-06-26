length_premise = 180 # from premise
length_hypothesis = 180 # from hypothesis

# check if the length of the carrier in the hypothesis matches the length mentioned in the premise
if length_hypothesis == length_premise:
    # if the lengths match, we can infer entailment
    label = "entailment"
else:
    # if the lengths do not match, we can infer contradiction or neutrality
    label = "contradiction" or "neutral"

print(label)
