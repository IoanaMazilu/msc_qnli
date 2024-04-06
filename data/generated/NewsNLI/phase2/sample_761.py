# Premise: One passenger paid $100,000 for the experience, with the majority paying between $1,500 and $5,000.
# Hypothesis: One passenger paid $100,000 for the first Singapore to Sydney trip.
# Golden Label: neutral

passenger_expense_premise = 100000
passenger_expense_hypothesis = 100000

# the hypothesis mentions the expense of one passenger for a trip, which is also referenced in the premise
# however, the hypothesis specifies the trip from Singapore to Sydney, which cannot be entailed from the premise
label = "neutral"

print(label)

