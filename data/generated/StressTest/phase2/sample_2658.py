# Premise: In 15 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Hypothesis: In less than 65 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Golden Label: entailment

years_future_premise = 15
years_future_hypothesis = 65

# the hypothesis refers to the same future time as the premise, but gives a different estimate
if years_future_hypothesis < years_future_premise:
    # check if the estimate of 'years_future_hypothesis' contradicts the time in the premise
    label = "contradiction"
elif years_future_hypothesis == years_future_premise:
    # if the hypothesis value is exactly the same as the premise one, we can infer entailment
    label = "entailment"
else:
    # the premise gives an exact time for the event
    # any time greater than 'years_future_premise' is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

