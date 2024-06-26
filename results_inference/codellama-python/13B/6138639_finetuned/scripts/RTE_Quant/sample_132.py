# premise:
gold_medals_premise = 18
world_records_premise = 21

# hypothesis:
gold_medals_hypothesis = 18
world_records_hypothesis = 21

# the hypothesis talks about the number of gold medals and world records won by Carl Lewis, which are also mentioned in the premise
if gold_medals_hypothesis!= gold_medals_premise:
    # check if the number of gold medals in the hypothesis contradicts the number of gold medals from the premise
    label = "contradiction"
elif world_records_hypothesis!= world_records_premise:
    # check if the number of world records in the hypothesis contradicts the number of world records from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
