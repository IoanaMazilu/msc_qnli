# Premise: Julie had more than 40 currency notes in all, some of which are of Rs 80 denomination and the remaining of Rs 50 denomination.
# Hypothesis: Julie had 90 currency notes in all, some of which are of Rs 80 denomination and the remaining of Rs 50 denomination.
# Golden Label: neutral

currency_notes_premise = 40
currency_notes_hypothesis = 90

# the hypothesis refers to the total number of currency notes Julie had, which is also mentioned in the premise
if currency_notes_hypothesis <= currency_notes_premise:
    # check if the number of 'currency_notes_hypothesis' contradicts the estimate of more than 'currency_notes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of currency notes
    # any number of currency notes greater than 'currency_notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

