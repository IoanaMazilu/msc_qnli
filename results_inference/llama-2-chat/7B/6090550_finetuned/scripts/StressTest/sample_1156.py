year_premise = 2979
year_hypothesis = 1979

# the hypothesis talks about the year in which the passengers were traveling, referenced also in the premise
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the years are the same, we can infer entailment
    label = "entailment"

print(label)
