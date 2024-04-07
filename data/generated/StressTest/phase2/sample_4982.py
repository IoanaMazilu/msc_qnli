# Premise: If the rosters for Professor Wang's 3 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Hypothesis: If the rosters for Professor Wang's 5 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Golden Label: contradiction

classes_premise = 3
classes_hypothesis = 5

# The hypothesis refers to a scenario of combining rosters for more classes than the premise.
if classes_hypothesis <= classes_premise:
    # Check if the number of classes in the hypothesis contradicts the premise.
    label = "contradiction"
else:
    # The premise does not provide a specific number of names for the combined roster.
    # Therefore, any number of combined classes greater than 'classes_premise' cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)

