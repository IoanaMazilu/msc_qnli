surplus_norway_premise = 4.61
surplus_south_korea_hypothesis = 7.01

# the hypothesis and premise mention the current account surplus of two different countries
# the premise gives the surplus for quarter 2 of 2017, while the hypothesis gives the surplus for June of 2017
if surplus_norway_premise!= surplus_south_korea_hypothesis:
    # check if the surplus of South Korea in the hypothesis contradicts the surplus of Norway in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
