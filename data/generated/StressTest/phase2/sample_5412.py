# Premise: Lary and Terry enter into a partnership by investing $700 and $300 respectively.
# Hypothesis: Lary and Terry enter into a partnership by investing $less than 800 and $300 respectively.
# Golden Label: entailment

investment_lary_premise = 700
investment_terry_premise = 300
investment_lary_hypothesis = 800
investment_terry_hypothesis = 300

# the hypothesis talks about the investments made by Lary and Terry, as mentioned in the premise
if investment_lary_hypothesis <= investment_lary_premise:
    # check if the hypothesis value contradicts the investment made by Lary as per the premise
    label = "contradiction"
elif investment_terry_premise != investment_terry_hypothesis:
    # check if the investment by Terry as per the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

