borrowed_years_premise = 4
borrowed_years_hypothesis = 8

# the hypothesis refers to the number of borrowed_years mentioned in the premise
if borrowed_years_hypothesis < borrowed_years_premise:
    # check if the estimate of 'borrowed_years_hypothesis' contradicts the number of borrowed years in the premise
    label = "contradiction"
elif borrowed_years_hypothesis == borrowed_years_premise:
    # check if the number of borrowed years in the hypothesis contradicts the number of borrowed years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
