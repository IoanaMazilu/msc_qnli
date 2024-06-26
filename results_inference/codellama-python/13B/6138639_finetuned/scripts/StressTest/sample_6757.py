p_goals_premise = 4
p_goals_hypothesis = 8

# the hypothesis talks about the number of P goals Tom goes after, referenced also in the premise
if p_goals_hypothesis <= p_goals_premise:
    # check if the hypothesis value contradicts the estimate of more than 'p_goals_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P goals
    # any number of P goals greater than 'p_goals_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
