less_than_premise = 750
sold_to_george_premise = 450
sold_to_george_hypothesis = 450

# the hypothesis talks about the amount of money she sold to George, which is also mentioned in the premise
if sold_to_george_hypothesis >= less_than_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif sold_to_george_hypothesis < less_than_premise:
    # if the hypothesis value is less than the premise, it is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it is neutral
    label = "neutral"

print(label)
