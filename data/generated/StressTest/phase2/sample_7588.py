# Premise: Calculate the average mark scored by Adam if he had the following scores in an examination:more than 46, 75, 72, 63 and 65 marks (out of 100) in French Language, Geography, Art and design, History and Physical Education respectively?
# Hypothesis: Calculate the average mark scored by Adam if he had the following scores in an examination:86, 75, 72, 63 and 65 marks (out of 100) in French Language, Geography, Art and design, History and Physical Education respectively?
# Golden Label: neutral

french_premise = 46
geography_premise = 75
art_design_premise = 72
history_premise = 63
phys_ed_premise = 65

french_hypothesis = 86
geography_hypothesis = 75
art_design_hypothesis = 72
history_hypothesis = 63
phys_ed_hypothesis = 65

# the hypothesis provides exact scores for all subjects, while the premise only gives an estimate for French
# first, we calculate the average scores based on the premise and hypothesis
average_premise = (french_premise + geography_premise + art_design_premise + history_premise + phys_ed_premise) / 5
average_hypothesis = (french_hypothesis + geography_hypothesis + art_design_hypothesis + history_hypothesis + phys_ed_hypothesis) / 5

if average_hypothesis < average_premise:
    # check if the average score calculated from the hypothesis contradicts the average score calculated from the premise
    label = "contradiction"
elif average_hypothesis == average_premise:
    # the premise gives only an estimate for the French score, while the hypothesis provides an exact score
    # if these exact scores lead to the same average as the premise, we cannot explicitly infer the hypothesis from the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the French score, while the hypothesis provides an exact score
    # any average score higher than the one calculated from the premise is consistent with the premise, but cannot be explicitly inferred from it
    label = "neutral"

print(label)

