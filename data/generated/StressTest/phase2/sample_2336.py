# Premise: Christine has 20 rs more than Siri.
# Hypothesis: Christine has less than 20 rs more than Siri.
# Golden Label: contradiction

christine_money_more_than_siri_premise = 20
christine_money_more_than_siri_hypothesis = 20

# the hypothesis talks about the difference in money between Christine and Siri, referenced also in the premise
if christine_money_more_than_siri_hypothesis >= christine_money_more_than_siri_premise:
    # check if the hypothesis value contradicts the statement of exactly 'christine_money_more_than_siri_premise' more than Siri
    label = "contradiction"
else:
    # the premise gives an exact amount for the difference in money
    # any amount less than 'christine_money_more_than_siri_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

