oppose_premise = 0.62
oppose_hypothesis = 0.63

# the hypothesis refers to the percentage of people who oppose U.S.-led efforts to fight terrorism, which is also mentioned in the premise
if oppose_hypothesis!= oppose_premise:
    # check if the percentage of people who oppose in the hypothesis contradicts the percentage of people who oppose in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
