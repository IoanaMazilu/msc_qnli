tom_investment_premise = 700
jerry_investment_premise = 300
tom_investment_hypothesis = 200
jerry_investment_hypothesis = 300

# the hypothesis refers to the same investments of Tom and Jerry mentioned in the premise
if tom_investment_hypothesis >= tom_investment_premise:
    # check if the estimate of 'tom_investment_hypothesis' contradicts the amount of Tom's investment in the premise
    label = "contradiction"
elif jerry_investment_hypothesis != jerry_investment_premise:
    # check if the amount of Jerry's investment in the hypothesis contradicts the amount of Jerry's investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
