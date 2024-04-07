# Premise: John has 13 ten-dollar bills, 11 five-dollar bills, and 17 one-dollar bills.
# Hypothesis: John has 63 ten-dollar bills, 11 five-dollar bills, and 17 one-dollar bills.
# Golden Label: contradiction

ten_dollar_bills_premise = 13
ten_dollar_bills_hypothesis = 63
five_dollar_bills_premise = 11
five_dollar_bills_hypothesis = 11
one_dollar_bills_premise = 17
one_dollar_bills_hypothesis = 17

# the hypothesis refers to the number of ten-dollar, five-dollar and one-dollar bills John has
if ten_dollar_bills_premise != ten_dollar_bills_hypothesis:
    # check if the number of ten-dollar bills in the hypothesis contradicts the number of ten-dollar bills mentioned in the premise
    label = "contradiction"
elif five_dollar_bills_premise != five_dollar_bills_hypothesis:
    # check if the number of five-dollar bills in the hypothesis contradicts the number of five-dollar bills mentioned in the premise
    label = "contradiction"
elif one_dollar_bills_premise != one_dollar_bills_hypothesis:
    # check if the number of one-dollar bills in the hypothesis contradicts the number of one-dollar bills mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

