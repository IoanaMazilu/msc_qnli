# Premise: John and Mike enter into a partnership by investing $700 and $300 respectively.
# Hypothesis: John and Mike enter into a partnership by investing $more than 700 and $300 respectively.
# Golden Label: contradiction

john_investment_premise = 700
john_investment_hypothesis = 700
mike_investment_premise = 300
mike_investment_hypothesis = 300

# the hypothesis refers to the investment amounts of John and Mike mentioned in the premise
if john_investment_premise != john_investment_hypothesis:
    # check if the investment amount of 'john_investment_hypothesis' contradicts the investment amount of John in the premise
    label = "contradiction"
elif mike_investment_hypothesis != mike_investment_premise:
    # check if the investment amount of Mike in the hypothesis contradicts the investment amount of Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

