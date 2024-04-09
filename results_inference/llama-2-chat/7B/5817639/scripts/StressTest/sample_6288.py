kiwi_fruit_premise = 8
kiwi_fruit_hypothesis = 5

# the hypothesis talks about the amount of kiwi fruit bought, which is also referenced in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the hypothesis value contradicts the estimate of 'kiwi_fruit_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the amount of kiwi fruit bought, but the hypothesis value does not contradict it
    label = "neutral"

print(label)
