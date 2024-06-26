latha_candies_premise = 10
ramu_candies_premise = 20
latha_candies_hypothesis = 20
ramu_candies_hypothesis = 20

# the hypothesis refers to the number of candies that Latha and Ramu have, mentioned also in the premise
if latha_candies_hypothesis <= latha_candies_premise:
    # check if the hypothesis value contradicts the number of candies Latha has in the premise
    label = "contradiction"
elif ramu_candies_hypothesis != ramu_candies_premise:
    # check if the number of candies Ramu has in the hypothesis contradicts the number of candies Ramu has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
