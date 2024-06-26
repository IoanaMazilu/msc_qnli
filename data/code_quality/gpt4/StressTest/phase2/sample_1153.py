death_percent_premise = 4
death_percent_hypothesis = 8
fearful_percent_premise = 15
fearful_percent_hypothesis = 15

# the hypothesis refers to the percent of people who died and those who left the village due to fear
if death_percent_hypothesis <= death_percent_premise and fearful_percent_hypothesis == fearful_percent_premise:
    # check if the percentage of deaths in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif death_percent_hypothesis > death_percent_premise and fearful_percent_hypothesis == fearful_percent_premise:
    # check if the percentage of deaths in the hypothesis can be entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
