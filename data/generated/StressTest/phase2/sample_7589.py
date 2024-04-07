# Premise: Calculate the average mark scored by Adam if he had the following scores in an examination:86, 75, 72, 63 and 65 marks (out of 100) in French Language, Geography, Art and design, History and Physical Education respectively?
# Hypothesis: Calculate the average mark scored by Adam if he had the following scores in an examination:more than 86, 75, 72, 63 and 65 marks (out of 100) in French Language, Geography, Art and design, History and Physical Education respectively?
# Golden Label: contradiction

# Define the scores of Adam in the premise
french_premise = 86
geography_premise = 75
art_design_premise = 72
history_premise = 63
physical_education_premise = 65

# Define the scores of Adam in the hypothesis
french_hypothesis = 86
geography_hypothesis = 75
art_design_hypothesis = 72
history_hypothesis = 63
physical_education_hypothesis = 65

# Calculate the average mark scored by Adam in the premise and hypothesis
average_premise = (french_premise + geography_premise + art_design_premise + history_premise + physical_education_premise) / 5
average_hypothesis = (french_hypothesis + geography_hypothesis + art_design_hypothesis + history_hypothesis + physical_education_hypothesis) / 5

# Check if the average score in the hypothesis is greater than the average score in the premise
if average_hypothesis > average_premise:
    # If the average score in the hypothesis is greater than the average score in the premise, it is a contradiction
    label = "contradiction"
elif average_hypothesis == average_premise:
    # If the average score in the hypothesis is equal to the average score in the premise, it is an entailment
    label = "entailment"
else:
    # If the average score in the hypothesis is less than the average score in the premise, it is neutral
    label = "neutral"

print(label)

