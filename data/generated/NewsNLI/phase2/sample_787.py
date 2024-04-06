# Premise: The United States committed over $800,000 for immediate humanitarian assistance to be provided through the United States Agency for International Development (USAID), according to the U.S. Embassy in Bishkek.
# Hypothesis: U.S. commits $1 million in assistance, supplies.
# Golden Label: neutral

assistance_premise = 800000
assistance_hypothesis = 1000000

# the hypothesis mentions the amount of assistance committed by the U.S., which is also mentioned in the premise
if assistance_hypothesis != assistance_premise:
    # check if the amount of assistance in the hypothesis contradicts the amount of assistance reported in the premise
    label = "contradiction"
else:
    # if the assistance value in the hypothesis does not contradict the assistance value in the premise, we infer entailment
    label = "entailment"

print(label)

