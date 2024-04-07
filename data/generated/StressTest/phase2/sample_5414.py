# Premise: Lary and Terry enter into a partnership by investing $700 and $300 respectively.
# Hypothesis: Lary and Terry enter into a partnership by investing $more than 700 and $300 respectively.
# Golden Label: contradiction

lary_investment_premise = 700
terry_investment_premise = 300
lary_investment_hypothesis = 700
terry_investment_hypothesis = 300

# the hypothesis talks about the investment amounts of Lary and Terry, referenced also in the premise
if lary_investment_hypothesis < lary_investment_premise:
    # check if 'lary_investment_hypothesis' contradicts the actual amount Lary invested in the premise
    label = "contradiction"
elif terry_investment_hypothesis != terry_investment_premise:
    # check if the investment amount of Terry in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
else:
    # the premise gives exact values for the investments
    # any amount of investment for Lary greater than 'lary_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

