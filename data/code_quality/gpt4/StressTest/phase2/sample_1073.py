tom_investment_premise = 700
jerry_investment_premise = 300
tom_investment_hypothesis = 700
jerry_investment_hypothesis = 300

# the hypothesis refers to the amount of investment made by Tom and Jerry, same as in the premise
if tom_investment_hypothesis == tom_investment_premise:
    # check if the hypothesis contradicts the premise about 'tom_investment_premise'
    label = "contradiction"
elif jerry_investment_hypothesis != jerry_investment_premise:
    # check if the hypothesis contradicts the premise about 'jerry_investment_premise'
    label = "contradiction"
else:
    # the premise gives specific investment amounts for Tom and Jerry, but the hypothesis contradicts Tom's investment
    label = "contradiction"

print(label)
