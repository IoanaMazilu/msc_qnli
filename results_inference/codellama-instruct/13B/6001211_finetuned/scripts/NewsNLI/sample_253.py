death_increase_premise = 500
death_increase_hypothesis = 5

# the hypothesis mentions the increase in the chance of death for women in domestic abuse situations if the abuser has access to a gun
# the premise also mentions this, but gives the increase as 500%, while the hypothesis states it as 5 times
# we cannot directly compare these two values, as they are not on the same scale

# to compare them, we need to convert the percentage increase in the premise to a similar multiplicative factor in the hypothesis
death_increase_premise_factor = (death_increase_premise / 100) + 1

if death_increase_premise_factor!= death_increase_hypothesis:
    # check if the multiplicative factor in the hypothesis contradicts the calculated factor from the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
