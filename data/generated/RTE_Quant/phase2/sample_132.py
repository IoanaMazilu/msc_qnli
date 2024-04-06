# Premise: More than a decade ago, Carl Lewis stood on the threshold of what was to become the greatest athletics career in history. He had just broken two of the legendary Jesse Owens'college records, but never believed he would become a corporate icon, the focus of hundreds of millions of dollars in advertising. His sport was still nominally amateur. Eighteen Olympic and World Championship gold medals and 21 world records later, Lewis has become the richest man in the history of track and field -- a multi-millionaire.
# Hypothesis: Carl Lewis won eighteen gold medals and set 21 world records.
# Golden Label: entailment

gold_medals_premise = 18
gold_medals_hypothesis = 18
world_records_premise = 21
world_records_hypothesis = 21

# the hypothesis talks about the number of gold medals won and world records set by Carl Lewis, which are also mentioned in the premise
if gold_medals_hypothesis != gold_medals_premise:
    # check if the number of gold medals in the hypothesis contradicts the number of gold medals from the premise
    label = "contradiction"
elif world_records_hypothesis != world_records_premise:
    # check if the number of world records in the hypothesis contradicts the number of world records in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

