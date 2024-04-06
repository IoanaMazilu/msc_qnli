# Premise: Violence over the last week killed 23 people, two worshippers dragged from a mosque and shot, underlining the challenges of bringing stability and strengthening Afghanistan's fledgling democracy.
# Hypothesis: Two worshippers were killed in Afghanistan.
# Golden Label: entailment

total_deaths_premise = 23
worshipper_deaths_premise = 2
worshipper_deaths_hypothesis = 2

# the hypothesis talks about the number of worshippers killed, which is also mentioned in the premise
if worshipper_deaths_hypothesis != worshipper_deaths_premise:
    # check if the number of worshippers deaths in the hypothesis contradicts the number of worshippers deaths from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

