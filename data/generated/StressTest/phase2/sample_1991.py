# Premise: Four different children have jelly beans:Aaron has 3, Bianca has 7, Callie has 8, and Dante has 11.
# Hypothesis: Four different children have jelly beans:Aaron has 5, Bianca has 7, Callie has 8, and Dante has 11.
# Golden Label: contradiction

aaron_jellybeans_premise = 3
bianca_jellybeans_premise = 7
callie_jellybeans_premise = 8
dante_jellybeans_premise = 11

aaron_jellybeans_hypothesis = 5
bianca_jellybeans_hypothesis = 7
callie_jellybeans_hypothesis = 8
dante_jellybeans_hypothesis = 11

# the hypothesis talks about the quantity of jelly beans each child has, which is also referenced in the premise
if (aaron_jellybeans_hypothesis != aaron_jellybeans_premise or
    bianca_jellybeans_hypothesis != bianca_jellybeans_premise or
    callie_jellybeans_hypothesis != callie_jellybeans_premise or
    dante_jellybeans_hypothesis != dante_jellybeans_premise):
    # check if the number of jelly beans each child has in the hypothesis contradicts the number of jelly beans mentioned in the premise
    label = "contradiction"
else:
    # if the number of jelly beans each child has in the hypothesis does not contradict the number of jelly beans mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

