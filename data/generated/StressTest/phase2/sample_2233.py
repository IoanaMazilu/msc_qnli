# Premise: Jancy had less than 200 currency notes in all, some of which are of Rs 70 denomination and the remaining of Rs 50 denomination.
# Hypothesis: Jancy had 100 currency notes in all, some of which are of Rs 70 denomination and the remaining of Rs 50 denomination.
# Golden Label: neutral

currency_notes_premise = 200
currency_notes_hypothesis = 100

# the hypothesis talks about the number of currency notes Jancy had, referenced also in the premise
if currency_notes_hypothesis >= currency_notes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'currency_notes_premise'
    label = "contradiction"
elif currency_notes_hypothesis < currency_notes_premise:
    # any number of notes less than 'currency_notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

