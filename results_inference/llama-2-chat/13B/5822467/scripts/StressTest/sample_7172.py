problems_solved_premise = range(70, 126)
problems_solved_hypothesis = range(40, 126)

# the hypothesis refers to the set of problems solved by Andy in the premise
if problems_solved_hypothesis.issubset(problems_solved_premise):
    # check if the hypothesis set is a subset of the premise set
    label = "entailment"
elif problems_solved_premise.issubset(problems_solved_hypothesis):
    # check if the premise set is a subset of the hypothesis set
    label = "contradiction"
else:
    # if the hypothesis set and premise set do not have any contradictory elements, we can infer neutrality
    label = "neutral"

print(label)
