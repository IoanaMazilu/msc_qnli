year_premise = 1921
year_hypothesis = 1921

# the hypothesis and premise mention the year when UK disposable income fell to its lowest
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
