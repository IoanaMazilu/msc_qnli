chairman_years_premise = 24
chairman_years_hypothesis = 24

# the hypothesis talks about the number of seasons Reinsdorf was the chairman of the White Sox which is also mentioned in the premise
if chairman_years_hypothesis != chairman_years_premise:
    # check if the number of seasons in the hypothesis contradicts the number of seasons in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
