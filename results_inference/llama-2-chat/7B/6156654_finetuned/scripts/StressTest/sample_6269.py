# the premise and hypothesis are about the same village and the same event
# however, the hypothesis adds an additional percentage of people who left the village

# compute the total number of people in the village
total_people_premise = 10 * 100 / 100
total_people_hypothesis = 10 * 100 / 100 + 20 * 100 / 100

# compute the number of people who died in the bombardment
dead_people_premise = total_people_premise * 0.1
dead_people_hypothesis = total_people_hypothesis * 0.1

# check if the number of people who died in the bombardment in the hypothesis contradicts the number of people who died in the bombardment in the premise
if dead_people_hypothesis!= dead_people_premise:
    label = "contradiction"
else:
    # if the number of people who died in the bombardment in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)
