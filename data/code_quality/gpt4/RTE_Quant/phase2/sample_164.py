jail_years_premise = 90
jail_years_hypothesis = 90

# the hypothesis talks about the number of years a U.S. soldier was sentenced to jail, which is also mentioned in the premise
if jail_years_hypothesis != jail_years_premise:
    # check if the number of jail years in the hypothesis contradicts the number of jail years from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)