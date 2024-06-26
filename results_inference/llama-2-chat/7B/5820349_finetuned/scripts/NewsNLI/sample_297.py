trapped_people_min_premise = 20
trapped_people_max_premise = 30
trapped_people_min_hypothesis = 20
trapped_people_max_hypothesis = 30

# the hypothesis mentions the possible number of people trapped in the casino, which is also referenced in the premise
if trapped_people_min_hypothesis < trapped_people_min_premise or trapped_people_max_hypothesis > trapped_people_max_premise:
    # check if the range of possible trapped people in the hypothesis contradicts the range reported in the premise
    label = "contradiction"
elif trapped_people_min_hypothesis > trapped_people_min_premise or trapped_people_max_hypothesis < trapped_people_max_premise:
    # check if the range of possible trapped people from the hypothesis is within the range reported in the premise
    label = "entailment"
else:
    # if the hypothesis range does not contradict or is within the premise range, we can infer neutrality
    label = "neutral"

print(label)
