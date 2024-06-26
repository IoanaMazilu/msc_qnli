# Define variables for the premise
sheep_num_premise = 0
horse_num_premise = 0
ratio_premise = 0

# Define variables for the hypothesis
sheep_num_hypothesis = 0
horse_num_hypothesis = 0
ratio_hypothesis = 0

# Extract numerical information from the premise
sheep_num_premise = int(re.search(r'\d+', premise).group())
horse_num_premise = int(re.search(r'\d+', premise).group())
ratio_premise = float(re.search(r'\d+.\d+', premise).group())

# Extract numerical information from the hypothesis
sheep_num_hypothesis = int(re.search(r'\d+', hypothesis).group())
horse_num_hypothesis = int(re.search(r'\d+', hypothesis).group())
ratio_hypothesis = float(re.search(r'\d+.\d+', hypothesis).group())

# Calculate the total number of horses and sheep
total_horses = horse_num_premise * ratio_premise
total_sheep = sheep_num_premise * ratio_premise

# Calculate the total number of horse food needed
total_horse_food = total_horses * 230

# Calculate the total number of sheep food needed
total_sheep_food = total_sheep * 230

# Calculate the total number of food needed
total_food = total_horse_food + total_sheep_food

# Check if the hypothesis values and estimates do not contradict the premise ones
if total_food <= 12880:
    label = "entailment"
else:
    label = "contradiction"

print(label)
