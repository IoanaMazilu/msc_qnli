potential_jurors_premise = 84
potential_jurors_hypothesis = 84
african_american_premise = 6
african_american_hypothesis = 6

# the hypothesis mentions the total number of potential jurors and the number of African-American ones, which are also mentioned in the premise
if potential_jurors_hypothesis!= potential_jurors_premise:
    # check if the total number of potential jurors in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif african_american_hypothesis!= african_american_premise:
    # check if the number of African-American jurors from the hypothesis contradicts the number of African-American jurors in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
