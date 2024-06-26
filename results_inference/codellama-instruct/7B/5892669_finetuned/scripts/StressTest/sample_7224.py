OA_premise = 2
AC_premise = 4
BD_premise = 6

OA_hypothesis = 6
AC_hypothesis = 4
BD_hypothesis = 6

# the hypothesis refers to the lengths of OA, AC and BD mentioned in the premise
if OA_premise >= OA_hypothesis:
    # check if the estimate of 'OA_hypothesis' contradicts the length of OA in the premise
    label = "contradiction"
elif AC_hypothesis!= AC_premise or BD_hypothesis!= BD_premise:
    # check if the lengths of AC and BD in the hypothesis contradict the lengths of AC and BD reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
