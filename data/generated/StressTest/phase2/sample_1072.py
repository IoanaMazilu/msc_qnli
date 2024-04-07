# Premise: Tom and Jerry enter into a partnership by investing $more than 200 and $300 respectively.
# Hypothesis: Tom and Jerry enter into a partnership by investing $700 and $300 respectively.
# Golden Label: neutral

tom_investment_premise = 200
jerry_investment_premise = 300
tom_investment_hypothesis = 700
jerry_investment_hypothesis = 300

# the hypothesis talks about the investment amount of Tom and Jerry, referenced also in the premise
if tom_investment_hypothesis <= tom_investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'tom_investment_premise'
    label = "contradiction"
elif jerry_investment_hypothesis != jerry_investment_premise:
    # check if the investment of Jerry in the hypothesis contradicts the investment of Jerry reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment of Tom
    # any investment of Tom greater than 'tom_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

