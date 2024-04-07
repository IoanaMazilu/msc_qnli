# Premise: Raman mixed 44 kg of butter at Rs.
# Hypothesis: Raman mixed less than 84 kg of butter at Rs.
# Golden Label: entailment

butter_kg_premise = 44
butter_kg_hypothesis = 84

# the hypothesis refers to the quantity of butter mixed by Raman, which is also mentioned in the premise
if butter_kg_hypothesis <= butter_kg_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif butter_kg_premise >= butter_kg_hypothesis:
    # check if the premise value contradicts the hypothesis value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, it is consistent but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

