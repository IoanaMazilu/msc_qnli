kiwi_fruit_premise = 5
kiwi_fruit_hypothesis = 8

# the hypothesis talks about the amount of kiwi fruit bought, which is also mentioned in the premise
if kiwi_fruit_hypothesis <= kiwi_fruit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'kiwi_fruit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of kiwi fruit bought
    # any amount of kiwi fruit greater than 'kiwi_fruit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
