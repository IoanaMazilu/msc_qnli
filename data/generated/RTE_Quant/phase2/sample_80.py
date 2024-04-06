# Premise: That was up from 3 percent in 2003 and marked the best showing since 1999, when the economy grew by 4.5 percent.
# Hypothesis: That was up from 3% in 2003 and marked the best showing since 1999, when the growth was 4.5%.
# Golden Label: entailment

growth_rate_2003_premise = 3
growth_rate_2003_hypothesis = 3
growth_rate_1999_premise = 4.5
growth_rate_1999_hypothesis = 4.5

# the hypothesis talks about the growth rates in two specific years, which is also mentioned in the premise
if growth_rate_2003_hypothesis != growth_rate_2003_premise:
    # check if the growth rate in 2003 in the hypothesis contradicts the growth rate in 2003 from the premise
    label = "contradiction"
elif growth_rate_1999_hypothesis != growth_rate_1999_premise:
    # check if the growth rate in 1999 in the hypothesis contradicts the growth rate in 1999 from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

