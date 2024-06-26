boats_premise = 3.0
people_premise = 5.0
people_hypothesis = 5.5

# the hypothesis refers to the average number of people in each boat, which is also mentioned in the premise
# compute the total number of people in the premise
total_people_premise = boats_premise * people_premise

if people_hypothesis > total_people_premise:
    # check if the number of people in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
elif people_hypothesis < total_people_premise:
    # check if the number of people in the hypothesis is less than the estimate of people in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
