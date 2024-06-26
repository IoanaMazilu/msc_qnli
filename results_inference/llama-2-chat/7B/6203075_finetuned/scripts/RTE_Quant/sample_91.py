people_living_with_hiv_premise = 39.4
people_living_with_hiv_hypothesis = 39.4

# the hypothesis and premise mention the number of people living with HIV
if people_living_with_hiv_hypothesis!= people_living_with_hiv_premise:
    # check if the number of people living with HIV in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
