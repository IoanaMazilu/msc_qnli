# Premise: While Haiyan killed more than 6,000 people, the Philippine government is blaming only two deaths on Hagupit so far.
# Hypothesis: Philippine government spokesman blames the cyclone for two deaths.
# Golden Label: neutral

deaths_haiyan_premise = 6000
deaths_hagupit_premise = 2
deaths_hagupit_hypothesis = 2

# the hypothesis mentions the number of deaths blamed on the cyclone, which is also mentioned in the premise
if deaths_hagupit_hypothesis != deaths_hagupit_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

