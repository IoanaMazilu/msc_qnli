# Premise: John has less than 83 ten-dollar bills, 11 five-dollar bills, and 17 one-dollar bills.
# Hypothesis: John has 13 ten-dollar bills, 11 five-dollar bills, and 17 one-dollar bills.
# Golden Label: neutral

ten_dollar_bills_premise = 83
ten_dollar_bills_hypothesis = 13
five_dollar_bills_premise = 11
five_dollar_bills_hypothesis = 11
one_dollar_bills_premise = 17
one_dollar_bills_hypothesis = 17

# the hypothesis provides specific numbers for each type of bills John has, mentioned also in the premise
if ten_dollar_bills_hypothesis >= ten_dollar_bills_premise:
    # check if the number of ten-dollar bills in the hypothesis contradicts the premise which specifies John has less than 'ten_dollar_bills_premise'
    label = "contradiction"
elif five_dollar_bills_hypothesis != five_dollar_bills_premise:
    # check if the number of five-dollar bills in the hypothesis contradicts the number of five-dollar bills reported in the premise
    label = "contradiction"
elif one_dollar_bills_hypothesis != one_dollar_bills_premise:
    # check if the number of one-dollar bills in the hypothesis contradicts the number of one-dollar bills reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

