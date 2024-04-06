# Premise: Governor Tim Pawlenty of Minnesota signed a bill into law on Thursday that requires the state to generate a significant amount of its energy needs from renewable sources. The amount of power generated by wind turbines in the state stands now at 895 megawatts.
# Hypothesis: The amount of power produced in Minnesota stands at 895 megawatts.
# Golden Label: neutral

power_generated_premise = 895
power_generated_hypothesis = 895

# the hypothesis specifies the total power produced in Minnesota, while the premise specifies power generated by wind turbines
# the hypothesis cannot be entailed from the premise, since the total power produced in Minnesota includes not only power from wind turbines.

label = "neutral"
print(label)
