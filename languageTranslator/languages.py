# Specify the file path
file_path = "languages.txt"

#####################################################
# Initialize an empty dictionary to store the data
lang_dict = {}

# Open the file in read mode
with open(file_path, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into a list using tab ('\t') as the separator
        row = line.strip().split('\t')

        # Check if the row has at least two elements (key and value)
        if len(row) >= 2:
            key = row[0]  # First column is the key
            value = row[1]  # Data after the first column are the values

            # Assign the key-value pair to the dictionary
            lang_dict[key] = value

lang_dict.update({'Portuguese (Brazil)': 'pt-BR'})
# Print the resulting dictionary
for key, value in lang_dict.items():
    print(f"{key}: {value}")



