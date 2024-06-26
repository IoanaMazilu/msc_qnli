physicians_premise = 10
physicians_hypothesis = 10

# the hypothesis mentions the number of physicians from across the country who disapprove of Oz being on the faculty, which is also referenced in the premise
if physicians_hypothesis!= physicians_premise:
    # check if the number of physicians in the hypothesis contradicts the number of physicians mentioned in the premise
    label = "contradiction"
else:
    # if the number of physicians in the hypothesis does not contradict the number of physicians in the premise, we can infer entailment
    label = "entailment"

print(label)
