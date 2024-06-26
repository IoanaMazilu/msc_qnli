fish_premise = 47.0
fish_given_premise = 22.0
fish_hypothesis = 25.0

# compute the difference between the premise and hypothesis values
diff = fish_premise - fish_hypothesis

# check if the difference is greater than 0 (contradiction) or less than 0 (entailment)
if diff > 0:
    label = "contradiction"
elif diff < 0:
    label = "entailment"
else:
    # if the difference is 0, there is no contradiction or entailment
    label = "neutral"

print(label)
