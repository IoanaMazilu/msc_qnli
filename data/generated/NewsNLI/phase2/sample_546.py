# Premise: Pastor Maldonado, who won the Spanish GP for Williams to become the fifth different winner this season in five races, qualified ninth fastest but was relegated 10 places.
# Hypothesis: Pastor Maldonado relegated 10 places for practice misdemeanor.
# Golden Label: neutral

relegation_premise = 10
relegation_hypothesis = 10

# the hypothesis mentions Pastor Maldonado's relegation, which is also mentioned in the premise
# however, the hypothesis refers to a practice misdemeanor as the cause of this relegation, which can't be entailed from the premise
label = "neutral"

print(label)

