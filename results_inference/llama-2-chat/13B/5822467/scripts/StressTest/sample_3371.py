# define variables for numerical entities in the premise and hypothesis
tshirts_premise = 8
avg_price_premise = float(input("Rs."))

# define variables for numerical entities in the hypothesis
tshirts_hypothesis = float(input("more than "))
avg_price_hypothesis = float(input("Rs."))

# compare the number of t-shirts sold in the premise and hypothesis
if tshirts_hypothesis > tshirts_premise:
    # the hypothesis contradicts the premise, as it states more t-shirts were sold
    label = "contradiction"
elif tshirts_hypothesis == tshirts_premise:
    # the hypothesis is neutral, as it does not contradict the premise
    label = "neutral"
else:
    # the premise states a specific number of t-shirts were sold, while the hypothesis states a range
    # any number of t-shirts within the range is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# compare the average price of t-shirts in the premise and hypothesis
if avg_price_hypothesis > avg_price_premise:
    # the hypothesis refers to a higher average price than the premise
    label = "entailment"
elif avg_price_hypothesis == avg_price_premise:
    # the hypothesis and premise have the same average price
    label = "neutral"
else:
    # the premise states a specific average price, while the hypothesis states a range
    # any price within the range is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
