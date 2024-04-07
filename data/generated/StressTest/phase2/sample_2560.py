# Premise: Tim and Jim enter into a partnership by investing $more than 300 and $300 respectively.
# Hypothesis: Tim and Jim enter into a partnership by investing $700 and $300 respectively.
# Golden Label: neutral

investment_tim_premise = 300
investment_tim_hypothesis = 700
investment_jim_premise = 300
investment_jim_hypothesis = 300

# the hypothesis refers to the investments made by Tim and Jim which are also mentioned in the premise
if investment_tim_hypothesis <= investment_tim_premise:
    # check if the investment value of Tim in the hypothesis contradicts the premise of more than 'investment_tim_premise'
    label = "contradiction"
elif investment_jim_hypothesis != investment_jim_premise:
    # check if the investment value of Jim in the hypothesis contradicts the investment value of Jim in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment of Tim
    # any investment value of Tim greater than 'investment_tim_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

