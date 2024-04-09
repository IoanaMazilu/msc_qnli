days_premise = less_than_40
days_hypothesis = 20

# the hypothesis refers to the number of days worked by the person in the premise
if days_hypothesis <= days_premise:
    # check if the estimate of 'days_hypothesis' contradicts the number of days worked in the premise
    label = "contradiction"
elif days_premise!= days_hypothesis:
    # check if the number of days worked in the hypothesis contradicts the number of days worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
