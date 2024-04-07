# Premise: If Ros é reads at a constant rate of 3 pages every 5 minutes, how many seconds will it take her to read N pages?
# Hypothesis: If Ros é reads at a constant rate of more than 1 pages every 5 minutes, how many seconds will it take her to read N pages?
# Golden Label: entailment

reading_rate_premise = 3 # pages every 5 minutes
reading_rate_hypothesis = 1 # pages every 5 minutes

# the hypothesis refers to the reading rate of Ros é, also mentioned in the premise
if reading_rate_hypothesis >= reading_rate_premise:
    # check if the hypothesis reading rate contradicts the reading rate in the premise
    label = "contradiction"
else:
    # if the hypothesis reading rate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

