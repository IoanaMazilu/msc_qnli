men_premise = 100
men_hypothesis = 200
highway_length_premise = 2
highway_length_hypothesis = 2
days_work_premise = 50
days_work_hypothesis = 50

# the hypothesis refers to the number of men and days of work mentioned in the premise
if men_hypothesis!= men_premise:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
elif days_work_hypothesis!= days_work_premise:
    # check if the number of days of work in the hypothesis contradicts the number of days of work reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
