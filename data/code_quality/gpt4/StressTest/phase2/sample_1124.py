# Scores obtained by Adam in different subjects as per the premise
Spanish_premise = 85
Mathematics_premise = 67
Biology_premise = 52
Physics_premise = 69
French_premise = 56
Fine_art_premise = 62
Chemistry_premise = 59

# Scores obtained by Adam in different subjects as per the hypothesis
Spanish_hypothesis = 85
Mathematics_hypothesis = 67
Biology_hypothesis = 52
Physics_hypothesis = 69
French_hypothesis = 56
Fine_art_hypothesis = 62
Chemistry_hypothesis = 59

# Calculating the average marks as per the premise and hypothesis
average_premise = (Spanish_premise + Mathematics_premise + Biology_premise + Physics_premise + French_premise + Fine_art_premise + Chemistry_premise) / 7
average_hypothesis = (Spanish_hypothesis + Mathematics_hypothesis + Biology_hypothesis + Physics_hypothesis + French_hypothesis + Fine_art_hypothesis + Chemistry_hypothesis) / 7

# Comparing the average marks as per premise and hypothesis
if average_hypothesis < average_premise:
    # If average marks as per hypothesis is less than average marks as per premise, it is contradiction
    label = "contradiction"
elif average_hypothesis == average_premise:
    # If average marks as per hypothesis is equal to average marks as per premise, it is entailment
    label = "entailment"
else:
    # If neither of the above conditions are met, it is neutral
    label = "neutral"

print(label)
