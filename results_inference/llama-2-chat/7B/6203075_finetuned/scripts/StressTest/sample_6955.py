average_shirts_premise = 80
average_shirts_hypothesis = 40
shirts_purchased_premise = 8
shirts_purchased_hypothesis = 8

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya, which is also mentioned in the premise
if average_shirts_hypothesis > average_shirts_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_shirts_hypothesis < average_shirts_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we cannot infer entailment or contradiction based on this information
    label = "neutral"

print(label)
