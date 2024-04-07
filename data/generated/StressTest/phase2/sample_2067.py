# Premise: When Robert's height is included, the average increases by 2 inches.
# Hypothesis: When Robert's height is included, the average increases by less than 5 inches.
# Golden Label: entailment

avg_increase_premise = 2
avg_increase_hypothesis = 5

# the hypothesis talks about the increase of the average when Robert's height is included, a situation also referred to in the premise
if avg_increase_hypothesis <= avg_increase_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif avg_increase_premise != avg_increase_hypothesis:
    # check if the average increase in the hypothesis is not the same as in the premise
    label = "neutral"
else:
    # if the hypothesis value and the premise are the same, we can infer entailment
    label = "entailment"

print(label)

