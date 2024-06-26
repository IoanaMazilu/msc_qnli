percentage_given_back_premise = 4
percentage_given_back_hypothesis = 6

# the hypothesis refers to the percentage given back, which is also mentioned in the premise
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the percentage given back in the hypothesis contradicts the percentage given back in the premise
    label = "contradiction"
elif percentage_given_back_hypothesis < percentage_given_back_premise:
    # if the percentage given back in the hypothesis is less than the premise, it can be entailed
    label = "entailment"
else:
    # if the percentage given back in the hypothesis is equal to the premise, it can't be explicitly entailed
    label = "neutral"

print(label)
