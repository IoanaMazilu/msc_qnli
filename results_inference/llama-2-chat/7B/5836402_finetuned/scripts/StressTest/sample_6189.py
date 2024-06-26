days_to_save_premise = 30
days_to_save_hypothesis = 80

# the hypothesis refers to the number of days Lexi needed to save for a vacation mentioned in the premise
if days_to_save_premise >= days_to_save_hypothesis:
    # check if the estimate of 'days_to_save_hypothesis' contradicts the number of days to save in the premise
    label = "contradiction"
elif days_to_save_hypothesis < days_to_save_premise:
    # check if the number of days to save in the hypothesis contradicts the number of days to save reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
