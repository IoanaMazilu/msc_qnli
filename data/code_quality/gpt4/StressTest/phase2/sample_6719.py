aaron_jellybeans_premise = 5
bianca_jellybeans_premise = 7
callie_jellybeans_premise = 8
dante_jellybeans_premise = 13

aaron_jellybeans_hypothesis = 2
bianca_jellybeans_hypothesis = 7
callie_jellybeans_hypothesis = 8
dante_jellybeans_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child mentioned in the premise has
if aaron_jellybeans_hypothesis != aaron_jellybeans_premise:
    # check if the number of jelly beans Aaron has in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif bianca_jellybeans_hypothesis != bianca_jellybeans_premise:
    # check if the number of jelly beans Bianca has in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif callie_jellybeans_hypothesis != callie_jellybeans_premise:
    # check if the number of jelly beans Callie has in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif dante_jellybeans_hypothesis != dante_jellybeans_premise:
    # check if the number of jelly beans Dante has in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
