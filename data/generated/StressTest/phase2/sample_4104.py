# Premise: Alex joined him 8 months later, investing Rs.
# Hypothesis: Alex joined him more than 7 months later, investing Rs.
# Golden Label: entailment

months_joined_premise = 8
months_joined_hypothesis = 7

# the hypothesis refers to the number of months Alex joined later, mentioned in the premise
if months_joined_hypothesis >= months_joined_premise:
    # check if the estimate of 'months_joined_hypothesis' contradicts the number of months mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

