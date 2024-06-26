# The hypothesis refers to the number of t-shirts returned by Sanoop and the average price of the remaining t-shirts
if sanoop_tshirts_returned > 8:
    # If the number of t-shirts returned by Sanoop is greater than 8, then the hypothesis is entailed
    label = "entailment"
elif sanoop_tshirts_returned == 8:
    # If the number of t-shirts returned by Sanoop is equal to 8, then the hypothesis is neutral
    label = "neutral"
else:
    # If the number of t-shirts returned by Sanoop is less than 8, then the hypothesis contradicts the premise
    label = "contradiction"

print(label)
