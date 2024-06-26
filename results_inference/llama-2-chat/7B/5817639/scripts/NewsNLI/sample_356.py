# Define variables for premise and hypothesis
gunshot_wounds_premise = 6
gunshot_wounds_hypothesis = 6

# Check if the number of gunshot wounds in the hypothesis matches the premise
if gunshot_wounds_hypothesis == gunshot_wounds_premise:
    # If the values match, we can infer entailment
    label = "entailment"
else:
    # If the values do not match, we can infer contradiction or neutrality
    if gunshot_wounds_hypothesis < gunshot_wounds_premise:
        label = "contradiction"
    else:
        label = "neutral"

print(label)
