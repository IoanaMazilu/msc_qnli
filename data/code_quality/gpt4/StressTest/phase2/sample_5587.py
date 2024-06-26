currency_notes_premise = 200
currency_notes_hypothesis = 100

# the hypothesis refers to the total number of currency notes Abinaya had, similar to the premise
if currency_notes_hypothesis >= currency_notes_premise:
    # check if the total number of currency notes in the hypothesis contradicts the estimate of less than 'currency_notes_premise'
    label = "contradiction"
elif currency_notes_hypothesis < currency_notes_premise:
    # if the total number of currency notes in the hypothesis is less than 'currency_notes_premise', it is consistent with the premise
    # but since the premise provides only an upper limit, the exact number cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
