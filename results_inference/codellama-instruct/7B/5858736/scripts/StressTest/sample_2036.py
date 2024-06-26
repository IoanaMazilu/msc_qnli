women_board_premise = 4
men_board_premise = 7

if women_board_premise <= men_board_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
