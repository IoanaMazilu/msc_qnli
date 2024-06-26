more_money_tim_premise = 800
more_money_tim_hypothesis = 600

# the hypothesis talks about the amount of money Tim received more than Jim, which is also referenced in the premise
if more_money_tim_hypothesis > more_money_tim_premise:
    # check if the hypothesis value contradicts the amount of money Tim received more than Jim in the premise
    label = "contradiction"
elif more_money_tim_hypothesis < more_money_tim_premise:
    # check if the hypothesis value is less than the amount of money Tim received more than Jim in the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise one, it's neutral
    label = "neutral"

print(label)
