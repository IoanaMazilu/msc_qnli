# Premise: Lary and Terry enter into a partnership by investing $less than 800 and $300 respectively.
# Hypothesis: Lary and Terry enter into a partnership by investing $700 and $300 respectively.
# Golden Label: neutral

investment_lary_premise = 800
investment_lary_hypothesis = 700
investment_terry_premise = 300
investment_terry_hypothesis = 300

# the hypothesis talks about the investment by Lary and Terry, referenced also in the premise
if investment_lary_hypothesis >= investment_lary_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_lary_premise' by Lary
    label = "contradiction"
elif investment_terry_hypothesis != investment_terry_premise:
    # check if the investment by Terry in the hypothesis contradicts the investment by Terry reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

