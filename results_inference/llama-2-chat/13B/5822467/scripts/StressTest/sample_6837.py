he_rick_earned_premise = 9000
he_rick_earned_hypothesis = 4000

# the hypothesis refers to the amount earned by he and Rick
if he_rick_earned_hypothesis <= he_rick_earned_premise:
    # check if the hypothesis value contradicts the estimate of more than 'he_rick_earned_premise'
    label = "contradiction"
elif he_rick_earned_hypothesis > he_rick_earned_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the amount earned
    # any amount greater than 'he_rick_earned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
