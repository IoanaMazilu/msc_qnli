premise_birds = 21.0
hypothesis_birds = 6.0

# compute the difference between the premise and hypothesis values
diff = premise_birds - hypothesis_birds

# check if the difference is greater than 0 (entailment) or less than 0 (contradiction)
if diff > 0:
    label = "entailment"
elif diff < 0:
    label = "contradiction"
else:
    # if the difference is 0, there is no contradiction or entailment
    label = "neutral"

print(label)
