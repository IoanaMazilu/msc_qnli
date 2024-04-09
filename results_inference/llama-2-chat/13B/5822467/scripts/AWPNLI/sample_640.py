fish_premise = 212.0
fish_hypothesis = 144.0

# compute the difference between the number of fish in the premise and the hypothesis
diff = fish_premise - fish_hypothesis

# check if the difference is negative (i.e., the hypothesis has a smaller number of fish than the premise)
if diff < 0:
    # if the difference is negative, the hypothesis contradicts the premise
    label = "contradiction"
elif diff == 0:
    # if the difference is zero, the hypothesis is neutral with respect to the premise
    label = "neutral"
else:
    # if the difference is positive (i.e., the hypothesis has a larger number of fish than the premise), we can infer entailment
    label = "entailment"

print(label)
