# Premise: Level-1 college graduates account for 10% of Listco's sales staff.
# Hypothesis: Level-less than 7 college graduates account for 10% of Listco's sales staff.
# Golden Label: entailment

level_1_graduates_premise = 10
level_7_graduates_hypothesis = 10

# the hypothesis talks about the percentage of level-7 graduates in the sales staff, while the premise talks about the percentage of level-1 graduates
# these two groups of graduates might not be the same (level-7 graduates may include level-1 ones, or not)
# thus, we cannot infer entailment or contradiction from the available information
label = "neutral"

print(label)

