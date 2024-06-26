year_premise = 1960
year_hypothesis = 1965

# the hypothesis refers to the year of lowest home ownership level, which is also mentioned in the premise
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis matches the year in the premise, we can infer entailment
    label = "entailment"

print(label)
