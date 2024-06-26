kiwi_fruit_premise = 5 * 360  # calculate the total weight of kiwi fruit in the premise
kiwi_fruit_hypothesis = 8 * 360

# check if the hypothesis value contradicts the premise estimate
if kiwi_fruit_hypothesis > kiwi_fruit_premise:
    label = "contradiction"
elif kiwi_fruit_hypothesis == kiwi_fruit_premise:
    # the hypothesis value is consistent with the premise estimate
    label = "neutral"
else:
    # the premise estimate is less than the hypothesis value, so we can entail the hypothesis
    label = "entailment"

print(label)
