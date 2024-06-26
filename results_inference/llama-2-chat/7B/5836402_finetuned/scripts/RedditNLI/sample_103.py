year_premise = 2008
year_hypothesis = 2006

# the premise and hypothesis mention the year when Mexico and Hong Kong raised their interest rates for the first time
if year_premise!= year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
