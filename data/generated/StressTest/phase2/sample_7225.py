# Premise: If OA = less than 6, AC = 4 and BD = 6, determine the length of OB.
# Hypothesis: If OA = 2, AC = 4 and BD = 6, determine the length of OB.
# Golden Label: neutral

OA_premise = 6
OA_hypothesis = 2
AC_premise = AC_hypothesis = 4
BD_premise = BD_hypothesis = 6

# the hypothesis refers to the lengths of OA, AC and BD mentioned in the premise
if OA_hypothesis >= OA_premise:
    # check if the estimate of 'OA_hypothesis' contradicts the number of OA in the premise
    label = "contradiction"
elif AC_hypothesis != AC_premise:
    # check if the length of AC in the hypothesis contradicts the length of AC reported in the premise
    label = "contradiction"
elif BD_hypothesis != BD_premise:
    # check if the length of BD in the hypothesis contradicts the length of BD reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

