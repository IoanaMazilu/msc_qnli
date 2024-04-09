bright_score_premise = 60
bivi_score_premise = 65
lisa_score_premise = 45

bright_score_hypothesis = float(input("Enter Bright's score: "))
bivi_score_hypothesis = float(input("Enter Bivi's score: "))
lisa_score_hypothesis = float(input("Enter Lisa's score: "))

# Check if the hypothesis values contradict the premise values
if bright_score_hypothesis > bright_score_premise:
    label = "entailment"
elif bivi_score_hypothesis == bivi_score_premise and lisa_score_hypothesis == lisa_score_premise:
    # The hypothesis values match the premise values, so there is no contradiction
    label = "neutral"
else:
    # At least one aspect in the hypothesis contradicts the premise
    label = "contradiction"

print(label)
