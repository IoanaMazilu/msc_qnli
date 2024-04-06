# Premise: The world's population is set to reach a staggering 10bn by the middle of 21st century up from 5.7bn now.
# Hypothesis: The world population will probably reach over 10 billion in 2050.
# Golden Label: entailment

population_premise = 10e9
population_hypothesis = 10e9
current_population_premise = 5.7e9

# the hypothesis talks about the world population reaching a certain number by a certain year (2050), which is not mentioned in the premise
# the premise talks about the world population reaching that same number but by the middle of the 21st century
# the precise year of the middle of the 21st century is not specified in the premise, hence we can't infer entailment or contradiction based on the year
# the world population estimate in the hypothesis does not contradict the estimate in the premise
label = "neutral"

print(label)

