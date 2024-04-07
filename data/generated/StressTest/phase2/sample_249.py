# Premise: Morgan Goldman has 5 Senior Managing Directors and 5 Managing Directors.
# Hypothesis: Morgan Goldman has more than 4 Senior Managing Directors and 5 Managing Directors.
# Golden Label: entailment

senior_directors_premise = 5
senior_directors_hypothesis = 4
managing_directors_premise = 5
managing_directors_hypothesis = 5

# the hypothesis refers to the number of senior and managing directors mentioned in the premise
if senior_directors_premise <= senior_directors_hypothesis:
    # check if the estimate of 'senior_directors_hypothesis' contradicts the number of senior directors in the premise
    label = "contradiction"
elif managing_directors_hypothesis != managing_directors_premise:
    # check if the number of managing directors in the hypothesis contradicts the number of managing directors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
