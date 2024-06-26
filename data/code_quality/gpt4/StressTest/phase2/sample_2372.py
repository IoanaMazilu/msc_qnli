ghana_win_probability_premise = 2/3
ghana_win_probability_hypothesis = 5/3

# the hypothesis refers to the probability of Ghana winning against Bolivia, which is also mentioned in the premise
if ghana_win_probability_premise == ghana_win_probability_hypothesis:
    # check if the probability of Ghana winning in the hypothesis matches with the probability mentioned in the premise
    label = "entailment"
elif ghana_win_probability_hypothesis > 1 or ghana_win_probability_hypothesis < ghana_win_probability_premise:
    # check if the probability of Ghana winning in the hypothesis contradicts the probability mentioned in the premise
    # as probabilities cannot be more than 1, a value of 5/3 for probability contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but also do not match exactly, we infer neutrality
    label = "neutral"

print(label)
