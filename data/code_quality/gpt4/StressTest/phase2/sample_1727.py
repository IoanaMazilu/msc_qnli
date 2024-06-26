senior_directors_premise = 4
senior_directors_hypothesis = 7
directors_premise = 5
directors_hypothesis = 5

# the hypothesis refers to the number of Senior Managing Directors and Managing Directors mentioned in the premise
if senior_directors_hypothesis != senior_directors_premise:
    # check if the number of Senior Managing Directors in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif directors_hypothesis != directors_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
