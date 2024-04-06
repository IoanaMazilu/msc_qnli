# Premise: Retaining the III Marine Expeditionary Force headquarters and some forces in Okinawa, the United States is shifting two Marine Air-Ground Task Forces (each comprising about 2,500 troops) to an emerging strategic hub in Guam, rotating another through Darwin, Australia, and basing supporting elements in Hawaii.
# Hypothesis: 9,000 Marines will be tranferred from Okinawa to Guam, Hawaii and Australia.
# Golden Label: neutral

force_headquarters_premise = 1
force_headquarters_hypothesis = 1
troops_moved_premise = 2 * 2500
troops_moved_hypothesis = 9000

# the hypothesis mentions the relocation of Marines from Okinawa to Guam, Hawaii, and Australia, which is also mentioned in the premise
# however, the hypothesis refers to a different number of troops being moved compared to the premise
if troops_moved_hypothesis != troops_moved_premise:
    # check if the number of troops moved in the hypothesis contradicts the number of troops moved reported in the premise
    label = "contradiction"
else:
    # if the number of troops moved does not contradict the premise, we check the force headquarters
    if force_headquarters_hypothesis != force_headquarters_premise:
        # check if the force headquarters in the hypothesis contradicts the force headquarters reported in the premise
        label = "contradiction"
    else:
        # if the number of troops moved and the force headquarters do not contradict the premise, we can infer entailment
        label = "entailment"

print(label)

