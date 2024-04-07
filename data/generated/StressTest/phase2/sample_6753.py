# Premise: Ana goes before 8 P.
# Hypothesis: Ana goes before more than 2 P.
# Golden Label: entailment

ana_goes_premise = 8
ana_goes_hypothesis = 2

# the hypothesis refers to the time when Ana goes, mentioned also in the premise
if ana_goes_hypothesis >= ana_goes_premise:
    # check if the estimate of 'ana_goes_hypothesis' contradicts the time when Ana goes in the premise
    label = "contradiction"
elif ana_goes_hypothesis < ana_goes_premise:
    # check if the time when Ana goes in the hypothesis is less than the time in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

