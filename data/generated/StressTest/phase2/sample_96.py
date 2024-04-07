# Premise: Warner Limited has 4 Senior Managing Directors and 6 Managing Directors.
# Hypothesis: Warner Limited has less than 8 Senior Managing Directors and 6 Managing Directors.
# Golden Label: entailment

senior_directors_premise = 4
directors_premise = 6
senior_directors_hypothesis = 8
directors_hypothesis = 6

# The hypothesis refers to the number of senior managing directors and managing directors at Warner Limited, also mentioned in the premise
if senior_directors_hypothesis < senior_directors_premise:
    # Check if the estimate of 'senior_directors_hypothesis' contradicts the number of senior managing directors in the premise
    label = "contradiction"
elif directors_hypothesis != directors_premise:
    # Check if the number of managing directors in the hypothesis contradicts the number of managing directors reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

