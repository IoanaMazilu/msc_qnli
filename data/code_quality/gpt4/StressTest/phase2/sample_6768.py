total_money_premise = 6600
total_money_hypothesis = 2600

# The hypothesis talks about the total amount of money distributed among John, Jose, and Binoy, which is also mentioned in the premise
if total_money_hypothesis >= total_money_premise:
    # check if the hypothesis value contradicts the total amount distributed in the premise
    label = "contradiction"
elif total_money_hypothesis < total_money_premise:
    # check if the total amount distributed in the hypothesis is less than the total amount distributed in the premise
    label = "entailment"
else:
    # any total amount distributed that doesn't contradict the premise can't be explicitly entailed from the premise
    label = "neutral"

print(label)
