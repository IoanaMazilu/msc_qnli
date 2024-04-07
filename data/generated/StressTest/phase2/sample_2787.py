# Premise: Raman mixed 24 kg of butter at Rs.
# Hypothesis: Raman mixed less than 34 kg of butter at Rs.
# Golden Label: entailment

butter_kg_premise = 24
butter_kg_hypothesis = 34

# the hypothesis refers to the amount of butter mixed mentioned in the premise
if butter_kg_premise >= butter_kg_hypothesis:
    # check if the value of 'butter_kg_premise' contradicts the estimate of less than 'butter_kg_hypothesis'
    label = "contradiction"
elif butter_kg_premise == butter_kg_hypothesis:
    # check if the value of 'butter_kg_premise' is exactly equal to 'butter_kg_hypothesis', which is also a contradiction as per the 'less' condition in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones and is less than the premise, we can infer entailment
    label = "entailment"

print(label)

