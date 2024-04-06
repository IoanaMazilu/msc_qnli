# Premise: Others put the toll much higher:The International Committee of the Red Cross said it's realistic to estimate that 10,000 people may have died nationally.
# Hypothesis: International Red Cross:Realistic to estimate 10,000 people dead across Philippines.
# Golden Label: neutral

death_toll_premise = 10000
death_toll_hypothesis = 10000

# the hypothesis mentions the estimated death toll, which is also mentioned in the premise
# the hypothesis also specifies the location (Philippines), which is not mentioned in the premise
if death_toll_hypothesis != death_toll_premise:
    # check if the death toll in the hypothesis contradicts the death toll reported in the premise
    label = "contradiction"
else:
    # if the death toll in the hypothesis does not contradict the death toll in the premise, we can infer neutrality as the location is not specified in the premise
    label = "neutral"

print(label)

