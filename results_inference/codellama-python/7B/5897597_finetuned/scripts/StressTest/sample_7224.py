OA_premise = 2
OA_hypothesis = 6
AC_premise = 4
AC_hypothesis = 4
BD_premise = 6
BD_hypothesis = 6

# the hypothesis refers to the lengths of OA, AC and BD mentioned in the premise
if OA_premise >= OA_hypothesis:
    # check if the estimate of 'OA_hypothesis' contradicts the length of OA in the premise
    label = "contradiction"
elif AC_premise!= AC_hypothesis or BD_premise!= BD_hypothesis:
    # check if the lengths of AC or BD in the hypothesis contradict the lengths reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
