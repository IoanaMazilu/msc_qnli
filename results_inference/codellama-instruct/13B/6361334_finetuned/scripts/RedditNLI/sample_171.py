# extract the year from the premise
year_premise = 1921

# extract the year from the hypothesis
year_hypothesis = 1921

# check if the year in the hypothesis contradicts the year in the premise
if year_hypothesis!= year_premise:
    label = "contradiction"
else:
    # if the year in the hypothesis is the same as the year in the premise, we can infer entailment
    label = "entailment"

print(label)
