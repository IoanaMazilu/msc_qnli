percentage_deaths_premise = 0.1
percentage_deaths_hypothesis = 0.3
percentage_fleeing_premise = 0.2
percentage_fleeing_hypothesis = 0.2

# the hypothesis refers to the percentage of deaths and fleeing people in a village, also mentioned in the premise
if percentage_deaths_hypothesis >= percentage_deaths_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_deaths_premise'
    label = "contradiction"
elif percentage_fleeing_hypothesis!= percentage_fleeing_premise:
    # check if the number of fleeing people in the hypothesis contradicts the number of fleeing people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
