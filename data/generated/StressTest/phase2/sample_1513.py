# Premise: John and Mike enter into a partnership by investing $more than 600 and $300 respectively.
# Hypothesis: John and Mike enter into a partnership by investing $700 and $300 respectively.
# Golden Label: neutral

john_investment_premise = 600
mike_investment_premise = 300
john_investment_hypothesis = 700
mike_investment_hypothesis = 300

# the hypothesis gives specific values for the investments of John and Mike, also mentioned in the premise
if john_investment_hypothesis <= john_investment_premise:
    # check if the investment amount for John in the hypothesis contradicts the premise which states it is more than 'john_investment_premise'
    label = "contradiction"
elif mike_investment_hypothesis != mike_investment_premise:
    # check if Mike's investment in the hypothesis contradicts the precise value given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment of John, so a specific value like 'john_investment_hypothesis' cannot be explicitly entailed from the premise
    # but it does not contradict the premise either
    label = "neutral"

print(label)

