# Premise: Dan leaves City A 120 minutes after Cara.
# Hypothesis: Dan leaves City A less than 420 minutes after Cara.
# Golden Label: entailment

dan_leaving_time_premise = 120
dan_leaving_time_hypothesis = 420

# the hypothesis refers to the time Dan leaves City A after Cara, mentioned in the premise
if dan_leaving_time_hypothesis < dan_leaving_time_premise:
    # check if the hypothesis value contradicts the time Dan leaves City A after Cara in the premise
    label = "contradiction"
elif dan_leaving_time_hypothesis == dan_leaving_time_premise:
    # check if the hypothesis value is the same as the time Dan leaves City A after Cara in the premise
    label = "entailment"
else:
    # the premise gives only an exact time for Dan leaving City A after Cara
    # any time less than 'dan_leaving_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

