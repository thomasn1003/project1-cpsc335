# Name: Thomas Nguyen
# CSUF Email: thomasn1003@csu.fullerton.edu
# Project 1 - Algorithm 1 for cpsc 335

def connecting_pairs_of_pers(row):
    swaps = 0
    n = len(row)  # Length of the row list
    
    # Loop through the row with a step of 2 
    for i in range(0, n, 2):
        if row[i] % 2 == 0:  # If the person is even
            # Check if the person is not seated with their correct partner
            if i + 1 < n and row[i + 1] != row[i] + 1:
                swaps += 1
                # Find the correct partner and swap
                for j in range(i + 2, n):
                    if row[j] == row[i] + 1:
                        row[i + 1], row[j] = row[j], row[i + 1]  # Swap them
                        break
        
        else:  # If the person is odd
            # Check if the person is not seated with their correct partner
            if i + 1 < n and row[i + 1] != row[i] - 1:
                swaps += 1
                # Find the correct partner and swap
                for j in range(i + 2, n):
                    if row[j] == row[i] - 1:
                        row[i + 1], row[j] = row[j], row[i + 1]  # Swap them
                        break
    
    return swaps  # Return the number of swaps made

def main():

    input_string = input("Enter the list for the seating arrangement: ")
    a = list(map(int, input_string.split()))
    result = connecting_pairs_of_pers(a)
    print(f"Number of swaps needed: {result}")

if __name__ == "__main__":
    main()