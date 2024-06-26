gold_medals_premise = 18
gold_medals_hypothesis = 18
world_records_premise = 21
world_records_hypothesis = 21

# the hypothesis mentions the number of gold medals and world records won by Carl Lewis
if gold_medals_hypothesis!= gold_medals_premise:
    label = "contradiction"
elif world_records_hypothesis!= world_records_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
