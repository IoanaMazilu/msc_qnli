aaron_jellybeans_premise = 7
bianca_jellybeans_premise = 7
callie_jellybeans_premise = 8
dante_jellybeans_premise = 11

aaron_jellybeans_hypothesis = 6
bianca_jellybeans_hypothesis = 7
callie_jellybeans_hypothesis = 8
dante_jellybeans_hypothesis = 11

# the hypothesis refers to the number of jelly beans each child has, as reported in the premise
if aaron_jellybeans_hypothesis >= aaron_jellybeans_premise:
    # check if the estimate for Aaron's jelly beans in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif bianca_jellybeans_hypothesis != bianca_jellybeans_premise:
    # check if the number of jelly beans Bianca has in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif callie_jellybeans_hypothesis != callie_jellybeans_premise:
    # check if the number of jelly beans Callie has in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif dante_jellybeans_hypothesis != dante_jellybeans_premise:
    # check if the number of jelly beans Dante has in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
