# Premise: John has 13 ten-dollar bills, 11 five-dollar bills, and 17 one-dollar bills.
# Hypothesis: John has less than 83 ten-dollar bills, 11 five-dollar bills, and 17 one-dollar bills.
# Golden Label: entailment

ten_dollar_bills_premise = 13
five_dollar_bills_premise = 11
one_dollar_bills_premise = 17

ten_dollar_bills_hypothesis = 83
five_dollar_bills_hypothesis = 11
one_dollar_bills_hypothesis = 17

# the hypothesis refers to the number of ten-dollar bills, five-dollar bills, and one-dollar bills John has according to the premise
if ten_dollar_bills_hypothesis <= ten_dollar_bills_premise:
    # check if the estimate of 'ten_dollar_bills_hypothesis' contradicts the number of ten-dollar bills John has according to the premise
    label = "contradiction"
elif five_dollar_bills_hypothesis != five_dollar_bills_premise:
    # check if the number of five-dollar bills in the hypothesis contradicts the number of five-dollar bills John has according to the premise
    label = "contradiction"
elif one_dollar_bills_hypothesis != one_dollar_bills_premise:
    # check if the number of one-dollar bills in the hypothesis contradicts the number of one-dollar bills John has according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

