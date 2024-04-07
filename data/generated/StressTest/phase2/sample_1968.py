# Premise: Morgan Construction has 4 Senior Managing Directors and 4 Managing Directors.
# Hypothesis: Morgan Construction has less than 5 Senior Managing Directors and 4 Managing Directors.
# Golden Label: entailment

senior_directors_premise = 4
senior_directors_hypothesis = 5
directors_premise = 4
directors_hypothesis = 4

# the hypothesis refers to the number of Senior Managing Directors and Managing Directors at Morgan Construction mentioned in the premise
if senior_directors_hypothesis <= senior_directors_premise:
    # check if the estimate of 'senior_directors_hypothesis' contradicts the number of Senior Managing Directors in the premise
    label = "contradiction"
elif directors_hypothesis != directors_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number of Managing Directors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

