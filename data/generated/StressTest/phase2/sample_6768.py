# Premise: 6600 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: more than 2600 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: entailment

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

