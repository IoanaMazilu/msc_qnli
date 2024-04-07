# Premise: Abinaya had 100 currency notes in all, some of which are of Rs 80 denomination and the remaining of Rs 50 denomination.
# Hypothesis: Abinaya had less than 200 currency notes in all, some of which are of Rs 80 denomination and the remaining of Rs 50 denomination.
# Golden Label: entailment

currency_notes_premise = 100
currency_notes_hypothesis = 200

# the hypothesis refers to the total number of currency notes Abinaya had, which is also mentioned in the premise
if currency_notes_hypothesis <= currency_notes_premise:
    # check if the hypothesis value contradicts the exact number of 'currency_notes_premise'
    label = "contradiction"
elif currency_notes_premise != currency_notes_hypothesis:
    # check if the total number of currency notes in the hypothesis contradicts the total number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

