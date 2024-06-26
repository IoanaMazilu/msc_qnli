# The premise and hypothesis both mention the number of t-shirts returned by Sanoop
# and the average price of the remaining t-shirts
if sanoop_returned_tshirts_premise < sanoop_returned_tshirts_hypothesis:
    # If the number of t-shirts returned by Sanoop in the premise is less than the number in the hypothesis,
    # then the hypothesis can be entailed from the premise
    label = "entailment"
else:
    # If the number of t-shirts returned by Sanoop in the premise is greater than or equal to the number in the hypothesis,
    # then the hypothesis cannot be entailed from the premise
    # Therefore, we mark it as neutral
    label = "neutral"

print(label)
