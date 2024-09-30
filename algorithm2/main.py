# Name: Thomas Nguyen
# CSUF Email: thomasn1003@csu.fullerton.edu
# Project 1 - Algorithm 1 for cpsc 335

def hamilton_problem(city_distances, fuel, mpg):
    n = len(city_distances) #how many cities
    total_gas = 0 
    total_distance = 0
    current_gas = 0
    start_index = 0
    
    # Loop through each city
    for i in range(n):
        # Calculate the total gas and distance
        total_gas += fuel[i]
        total_distance += city_distances[i]
        
        # Calculate the current gas at the starting index
        current_gas += fuel[i] - (city_distances[i] / mpg)
        
        # If current_gas is negative, reset the starting index
        if current_gas < 0:
            start_index = i + 1
            current_gas = 0
    
    return start_index

def main():
    
    input_cities = input("Enter the distances for the cities in order(seperated by space): ")
    city_dist = list(map(int, input_cities.split()))

    input_fuel = input("Enter the fuel amounts each city has in order(seperated by space): ")
    city_fuel = list(map(int, input_fuel.split()))

    input_mpg = int(input("Enter the mpg of the vehicle: "))

    result = hamilton_problem(city_dist, city_fuel, input_mpg)
    
    print(f"The preferred starting city for the sample above is city {result}")

if __name__ == "__main__":
    main()
