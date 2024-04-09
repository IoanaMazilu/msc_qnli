salman_shirts_premise = 40
salman_shirts_hypothesis = 80
ambani_shirts_premise = 40
ambani_shirts_hypothesis = 80
dalmiya_shirts_premise = 40
dalmiya_shirts_hypothesis = 80

# define variables for the number of shirts purchased by each person
salman_shirts_purchased = 8
ambani_shirts_purchased = 8
dalmiya_shirts_purchased = 8

# calculate the average number of shirts for each person
salman_average_shirts = salman_shirts_purchased / 3
ambani_average_shirts = ambani_shirts_purchased / 3
dalmiya_average_shirts = dalmiya_shirts_purchased / 3

# compare the average number of shirts for each person in the hypothesis and premise
if salman_average_shirts <= salman_shirts_hypothesis:
    # the hypothesis value contradicts the estimate of Salman's average number of shirts in the premise
    label = "contradiction"
elif ambani_average_shirts!= ambani_shirts_hypothesis:
    # the hypothesis value contradicts the estimate of Aambani's average number of shirts in the premise
    label = "contradiction"
elif dalmiya_average_shirts!= dalmiya_shirts_hypothesis:
    # the hypothesis value contradicts the estimate of Dalmiya's average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
