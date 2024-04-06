# Premise: Fifteen percent said they have a favorable view of al Qaeda's leader, Saudi exile Osama bin Laden, the poll found.
# Hypothesis: Survey:10 percent of Saudis polled have a favorable view of al Qaeda.
# Golden Label: neutral

favorable_view_bin_laden_premise = 0.15
favorable_view_al_qaeda_hypothesis = 0.10

# the hypothesis mentions the favorable view percentage of al Qaeda, while the premise mentions the favorable view percentage of al Qaeda's leader
# we cannot directly compare these two quantities as they refer to different subjects
label = "neutral"

print(label)

