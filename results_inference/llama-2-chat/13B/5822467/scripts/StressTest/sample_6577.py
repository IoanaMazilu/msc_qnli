shirt_rate_premise = float(input("Premise: Vijay bought less than 560 shirts at the rate of Rs. "))
shirt_rate_hypothesis = float(input("Hypothesis: Vijay bought 160 shirts at the rate of Rs. "))

# compare the two rates
if shirt_rate_hypothesis < shirt_rate_premise:
    # the hypothesis rate is lower than the premise rate, so there is no contradiction
    label = "neutral"
elif shirt_rate_hypothesis > shirt_rate_premise:
    # the hypothesis rate is higher than the premise rate, so there is a contradiction
    label = "contradiction"
else:
    # the hypothesis rate is the same as the premise rate, so there is entailment
    label = "entailment"

print(label)
