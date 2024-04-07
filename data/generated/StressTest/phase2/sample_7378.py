# Premise: Mr Yadav spends more than 20% of his monthly salary on consumable items and 50% of the remaining on clothes and transport.
# Hypothesis: Mr Yadav spends 60% of his monthly salary on consumable items and 50% of the remaining on clothes and transport.
# Golden Label: neutral

consumable_items_expense_premise = 20
consumable_items_expense_hypothesis = 60
clothes_and_transport_expense_premise = 50
clothes_and_transport_expense_hypothesis = 50

# hypothesis and premise both talk about the percentage of Mr Yadav's salary spent on consumable items and on clothes and transport
if consumable_items_expense_hypothesis <= consumable_items_expense_premise:
    # check if the hypothesis value contradicts the premise which states that the consumable items expense is more than 'consumable_items_expense_premise'
    label = "contradiction"
elif clothes_and_transport_expense_hypothesis != clothes_and_transport_expense_premise:
    # check if the percentage of salary spent on clothes and transport according to the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives an estimate (more than 20%) for the consumable items expense
    # any percentage greater than 'consumable_items_expense_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

