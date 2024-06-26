year_premise = 2979
year_hypothesis = 1979

# the hypothesis refers to the year when the passengers were traveling, which is also mentioned in the premise
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis does not contradict the year in the premise, we can infer entailment
    label = "entailment"

print(label)
