% entailment, contradiction, neutral

premise = "In ABC limited, 75% are using Samsung phone at the same time 70% using i phone ; If in the same company 85% are using Samsung phone then, what is the percentage of i phone user?"
hypothesis = "In ABC limited, less than 75% are using Samsung phone at the same time 70% using i phone ; If in the same company 85% are using Samsung phone then, what is the percentage of i phone user?"

# extract variables from premise and hypothesis
samsung_premise = 75
samsung_hypothesis = 75
iphone_premise = 70
iphone_hypothesis = 70

# calculate the difference between samsung and iphone usage in the premise
samsung_diff = samsung_hypothesis - samsung_premise

# check if the difference between samsung and iphone usage in the premise contradicts the hypothesis
if samsung_diff > 0:
    label = "contradiction"
elif samsung_diff == 0:
    # if the difference between samsung and iphone usage in the premise is zero, it means that the hypothesis is neutral
    label = "neutral"
else:
    # if the difference between samsung and iphone usage in the premise is less than zero, it means that the hypothesis entails the premise
    label = "entailment"

print(label)
