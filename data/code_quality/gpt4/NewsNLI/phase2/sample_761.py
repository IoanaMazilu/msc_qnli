passenger_expense_premise = 100000
passenger_expense_hypothesis = 100000

# the hypothesis mentions the expense of one passenger for a trip, which is also referenced in the premise
# however, the hypothesis specifies the trip from Singapore to Sydney, which cannot be entailed from the premise
label = "neutral"

print(label)
