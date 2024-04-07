# Premise: Calculate the average mark scored by Adam if he had the following scores in an examination:more than 15, 67, 52, 69, 56, 62, and 59 marks (out in 100) in Spanish Language, Mathematics, Biology, Physics, French Language, Fine art and Chemistry respectively?
# Hypothesis: Calculate the average mark scored by Adam if he had the following scores in an examination:85, 67, 52, 69, 56, 62, and 59 marks (out in 100) in Spanish Language, Mathematics, Biology, Physics, French Language, Fine art and Chemistry respectively?
# Golden Label: neutral

# Scores in different subjects according to the premise
spanish_premise = 15
mathematics_premise = 67
biology_premise = 52
physics_premise = 69
french_premise = 56
fine_art_premise = 62
chemistry_premise = 59

# Scores in different subjects according to the hypothesis
spanish_hypothesis = 85
mathematics_hypothesis = 67
biology_hypothesis = 52
physics_hypothesis = 69
french_hypothesis = 56
fine_art_hypothesis = 62
chemistry_hypothesis = 59

# Calculate the average scores according to premise and hypothesis
average_premise = (spanish_premise + mathematics_premise + biology_premise + physics_premise + french_premise + fine_art_premise + chemistry_premise) / 7
average_hypothesis = (spanish_hypothesis + mathematics_hypothesis + biology_hypothesis + physics_hypothesis + french_hypothesis + fine_art_hypothesis + chemistry_hypothesis) / 7

# Check if the average scores contradict each other
if average_hypothesis <= average_premise:
    label = "contradiction"
elif spanish_hypothesis <= spanish_premise:
    # Check if spanish score in hypothesis contradicts the premise
    label = "contradiction"
else:
    label = "neutral"

print(label)

