# Premise: Four different children have jelly beans:Aaron has 5, Bianca has 7, Callie has 8, and Dante has 19.
# Hypothesis: Four different children have jelly beans:Aaron has less than 8, Bianca has 7, Callie has 8, and Dante has 19.
# Golden Label: entailment

aaron_beans_premise = 5
aaron_beans_hypothesis = 8
bianca_beans_premise = 7
bianca_beans_hypothesis = 7
callie_beans_premise = 8
callie_beans_hypothesis = 8
dante_beans_premise = 19
dante_beans_hypothesis = 19

# the hypothesis refers to the same children and their jelly beans as stated in the premise
if aaron_beans_hypothesis <= aaron_beans_premise:
    # check if Aaron's number of beans in the hypothesis contradicts the number of beans he has in the premise
    label = "contradiction"
elif bianca_beans_hypothesis != bianca_beans_premise:
    # check if Bianca's number of beans in the hypothesis contradicts the number of beans she has in the premise
    label = "contradiction"
elif callie_beans_hypothesis != callie_beans_premise:
    # check if Callie's number of beans in the hypothesis contradicts the number of beans she has in the premise
    label = "contradiction"
elif dante_beans_hypothesis != dante_beans_premise:
    # check if Dante's number of beans in the hypothesis contradicts the number of beans he has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

