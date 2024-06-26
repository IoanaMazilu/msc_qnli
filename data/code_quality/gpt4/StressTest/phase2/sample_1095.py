coffee_premise = 130
coffee_hypothesis = 230

# the hypothesis talks about the amount of coffee Carina has, which is also mentioned in the premise
if coffee_hypothesis <= coffee_premise:
    # check if the hypothesis value contradicts the actual amount of coffee in the premise
    label = "contradiction"
elif coffee_premise > coffee_hypothesis:
    # check if the amount of coffee in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise amount of coffee
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
