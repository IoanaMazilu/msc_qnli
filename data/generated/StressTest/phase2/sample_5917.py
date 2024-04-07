# Premise: If Jerry wants to raise his average by less than 7 points, what score must he earn on the fourth test?
# Hypothesis: If Jerry wants to raise his average by 2 points, what score must he earn on the fourth test?
# Golden Label: neutral

raise_avg_premise = 7
raise_avg_hypothesis = 2

# the hypothesis talks about raising the average score, which is also mentioned in the premise
if raise_avg_hypothesis >= raise_avg_premise:
    # check if 'raise_avg_hypothesis' contradicts the estimate of less than 'raise_avg_premise'
    label = "contradiction"
elif raise_avg_hypothesis == raise_avg_premise:
    # if the average raise in the hypothesis is exactly equal to the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the raise in average
    # any raise in average less than 'raise_avg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

