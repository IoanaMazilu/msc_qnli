# Premise: Kellogg's ended its Michael Phelps endorsement, so it sent two tons of cereal with his face on it to a food bank.
# Hypothesis: Kellogg's donated two tons of cereal to the San Francisco Food Bank.
# Golden Label: entailment

cereal_donation_premise = 2
cereal_donation_hypothesis = 2

# the hypothesis mentions the amount of cereal donated by Kellogg's, which is also mentioned in the premise
# however, the hypothesis does not specify that the cereal boxes featured Michael Phelps, which is a detail from the premise
# additionally, the premise does not specify the food bank's location, while the hypothesis states it was the San Francisco Food Bank
label = "neutral"

print(label)

