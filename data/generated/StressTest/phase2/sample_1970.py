# Premise: Morgan Construction has 4 Senior Managing Directors and 4 Managing Directors.
# Hypothesis: Morgan Construction has more than 4 Senior Managing Directors and 4 Managing Directors.
# Golden Label: contradiction

senior_directors_premise = 4
senior_directors_hypothesis = 4
managing_directors_premise = 4
managing_directors_hypothesis = 4

# the hypothesis refers to the number of senior and managing directors in Morgan Construction 
if senior_directors_hypothesis != senior_directors_premise:
    # check if the number of senior directors in the hypothesis contradicts the number of senior directors in the premise
    label = "contradiction"
elif managing_directors_hypothesis != managing_directors_premise:
    # check if the number of managing directors in the hypothesis contradicts the number of managing directors in the premise
    label = "contradiction"
else:
    # if the hypothesis values contradict the premise ones, we can infer contradiction
    label = "contradiction"

print(label)

