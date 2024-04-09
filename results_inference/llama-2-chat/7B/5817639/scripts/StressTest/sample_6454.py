# Variables for premise and hypothesis
english_premise = 76
english_hypothesis = 66
mathematics_premise = 60
mathematics_hypothesis = 60
chemistry_premise = 72
chemistry_hypothesis = 72
biology_premise = 77
biology_hypothesis = 77
french_language_premise = 55
french_language_hypothesis = 55
physics_premise = 85
physics_hypothesis = 85

# Comparison between premise and hypothesis values
if english_hypothesis <= english_premise:
    # Check if the estimate of 'english_hypothesis' contradicts the number of scored marks in the premise
    label = "contradiction"
elif mathematics_hypothesis!= mathematics_premise:
    # Check if the number of scored marks in the hypothesis contradicts the number of scored marks reported in the premise
    label = "contradiction"
elif chemistry_hypothesis!= chemistry_premise:
    # Check if the number of scored marks in the hypothesis contradicts the number of scored marks reported in the premise
    label = "contradiction"
elif biology_hypothesis!= biology_premise:
    # Check if the number of scored marks in the hypothesis contradicts the number of scored marks reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
