# Premise: Calculate the average mark scored by Andrea if he had the following scores in an examination:66, 60, 72, 77, 55 and 85 marks (out of 100) in English, Mathematics, Chemistry, Biology, French Language and Physics respectively?
# Hypothesis: Calculate the average mark scored by Andrea if he had the following scores in an examination:less than 76, 60, 72, 77, 55 and 85 marks (out of 100) in English, Mathematics, Chemistry, Biology, French Language and Physics respectively?
# Golden Label: entailment

english_score_premise = 66
math_score_premise = 60
chem_score_premise = 72
bio_score_premise = 77
french_score_premise = 55
physics_score_premise = 85

english_score_hypothesis = 76
math_score_hypothesis = 60
chem_score_hypothesis = 72
bio_score_hypothesis = 77
french_score_hypothesis = 55
physics_score_hypothesis = 85

avg_score_premise = (english_score_premise + math_score_premise + chem_score_premise + bio_score_premise + french_score_premise + physics_score_premise) / 6
avg_score_hypothesis = (english_score_hypothesis + math_score_hypothesis + chem_score_hypothesis + bio_score_hypothesis + french_score_hypothesis + physics_score_hypothesis) / 6

# Compare the averages calculated from the scores in the premise and hypothesis
if avg_score_hypothesis > avg_score_premise:
    # If the average score in the hypothesis is more than the average score in the premise, it is a contradiction
    label = "contradiction"
elif avg_score_hypothesis < avg_score_premise:
    # If the average score in the hypothesis is less than the average score in the premise, it is an entailment
    label = "entailment"
else:
    # If the average scores in the premise and hypothesis are equal, it is neutral
    label = "neutral"

print(label)

