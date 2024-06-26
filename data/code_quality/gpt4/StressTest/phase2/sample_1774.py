suman_year_premise = 1009
suman_year_hypothesis = 2009

# the hypothesis refers to the year of Suman's income mentioned in the premise
if suman_year_premise != suman_year_hypothesis:
    # check if the year in the hypothesis contradicts the year reported in the premise
    label = "contradiction"
else:
    # if the hypothesis year does not contradict the premise year, we can infer entailment
    label = "entailment"

print(label)