# Premise: Fairleigh Dickinson University's Public Mind Poll found that Clinton garnered 45% of the New Jersey electorate while Christie won 42%.
# Hypothesis: Poll gives Clinton 45% of New Jersey electorate, compared to Christie's 42 %.
# Golden Label: entailment

clinton_premise = 0.45
christie_premise = 0.42
clinton_hypothesis = 0.45
christie_hypothesis = 0.42

# the hypothesis mentions the percentage of the New Jersey electorate that support Clinton and Christie, which are also mentioned in the premise
if clinton_hypothesis != clinton_premise:
    # check if the percentage for Clinton in the hypothesis contradicts the percentage for Clinton reported in the premise
    label = "contradiction"
elif christie_hypothesis != christie_premise:
    # check if the percentage for Christie from the hypothesis contradicts the percentage for Christie in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

