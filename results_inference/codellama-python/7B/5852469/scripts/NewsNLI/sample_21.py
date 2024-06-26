years_premise = 75
years_hypothesis = 75

# the hypothesis mentions the number of years of the NBA, which is also mentioned in the premise
if years_hypothesis!= years_premise:
    # check if the number of years from the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
