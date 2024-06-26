amount_premise = float(input("Amount of money in the premise: "))
amount_hypothesis = float(input("Amount of money in the hypothesis: "))

# The hypothesis refers to the ratio of money to be divided between Priya, Mani, and Rani
if amount_hypothesis <= amount_premise:
    # Check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # The premise only provides an estimate for the ratio, and any ratio consistent with that estimate is consistent with the premise
    label = "neutral"

print(label)
