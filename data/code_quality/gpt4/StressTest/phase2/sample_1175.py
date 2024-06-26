discount_premise = 30
discount_hypothesis = 30

# Both premise and hypothesis talk about the same discount applied on the article that Jeevan bought
if discount_hypothesis > discount_premise:
    # Check if the discount in the hypothesis contradicts the discount mentioned in the premise
    label = "contradiction"
elif discount_hypothesis == discount_premise:
    # Check if the discount in the hypothesis matches the discount mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis discount is less than the premise discount, it doesn't contradict the premise but can't be explicitly entailed from the premise either
    label = "neutral"

print(label)
