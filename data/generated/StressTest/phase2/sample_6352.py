# Premise: If the profit in the business at the end of the year was less than 42000 how much amount would Mr Praveen have received as the profit?
# Hypothesis: If the profit in the business at the end of the year was 22000 how much amount would Mr Praveen have received as the profit?
# Golden Label: neutral

profit_premise = 42000
profit_hypothesis = 22000

# the hypothesis makes a reference to a possible profit value also mentioned in the premise
if profit_hypothesis >= profit_premise:
    # check if the value of 'profit_hypothesis' contradicts the estimate of less than 'profit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit
    # any profit value less than 'profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

