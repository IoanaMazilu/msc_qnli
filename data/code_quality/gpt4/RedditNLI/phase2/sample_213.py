min_wage_premise = 15
min_wage_hypothesis = 15

# the hypothesis and premise mention the same minimum wage
if min_wage_premise != min_wage_hypothesis:
    # check if the minimum wage in the hypothesis contradicts the minimum wage in the premise
    label = "contradiction"
else:
    # the premise and hypothesis do not contradict each other, but the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
