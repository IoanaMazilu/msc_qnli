# Define variables with representative names for the numerical entities in both inputs
french_score_premise = 86
french_score_hypothesis = float(input("Enter a score for French Language: "))
geography_score_premise = 75
geography_score_hypothesis = float(input("Enter a score for Geography: "))
art_design_score_premise = 72
art_design_score_hypothesis = float(input("Enter a score for Art and Design: "))
history_score_premise = 63
history_score_hypothesis = float(input("Enter a score for History: "))
physical_education_score_premise = 65
physical_education_score_hypothesis = float(input("Enter a score for Physical Education: "))

# Extract all quantities as valid numbers (integers or floats)
# and perform calculations if necessary
total_french_score_premise = french_score_premise + geography_score_premise + art_design_score_premise + history_score_premise + physical_education_score_premise
total_french_score_hypothesis = french_score_hypothesis + geography_score_hypothesis + art_design_score_hypothesis + history_score_hypothesis + physical_education_score_hypothesis

# Compare the total scores
if total_french_score_hypothesis > total_french_score_premise:
    # The hypothesis contradicts the premise
    label = "contradiction"
elif total_french_score_hypothesis < total_french_score_premise:
    # The hypothesis is inconsistent with the premise
    label = "neutral"
else:
    # The hypothesis and premise are consistent, so we can infer entailment
    label = "entailment"

print(label)
