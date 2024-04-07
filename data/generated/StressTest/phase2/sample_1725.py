# Premise: Apple Infotech has 4 Senior Managing Directors and 5 Managing Directors.
# Hypothesis: Apple Infotech has less than 6 Senior Managing Directors and 5 Managing Directors.
# Golden Label: entailment

senior_directors_premise = 4
senior_directors_hypothesis = 6
managing_directors_premise = 5
managing_directors_hypothesis = 5

# the hypothesis refers to the number of senior and managing directors at Apple Infotech mentioned in the premise
if senior_directors_hypothesis <= senior_directors_premise:
    # check if the estimate of 'senior_directors_hypothesis' contradicts the number of senior directors in the premise
    label = "contradiction"
elif managing_directors_hypothesis != managing_directors_premise:
    # check if the number of managing directors in the hypothesis contradicts the number of managing directors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

