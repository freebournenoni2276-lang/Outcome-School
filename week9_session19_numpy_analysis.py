import numpy as np  # Import the NumPy library for numerical operations

# Create a class to analyze numerical data
class NumericAnalyzer:

    # Constructor method to initialize variables when the class is created
    def __init__(self, daily_temps):
        self.daily_temps = daily_temps  
        self.data = None  
        self.multiply_data = None  
        self.add_to_data = None  
        self.reshape_data = None   
        self.filter_data = None  
        self.min_data = None  
        self.max_data = None  
        self.avg_data = None  


    # Method to create the dataset
    def create_data(self):

        # Only create the dataset if it has not been created yet
        if self.data is None:
            print(f"\nDataset: {self.daily_temps}")
            print("\nCreating Data.....")

            # Create a list of daily temperatures
            temps = [28,31,24,30,27,22,33,26]

            # Convert the list into a NumPy array
            self.data = np.array(temps)

            print("\nDaily Temperatures:")
            print(self.data)


    # Method to perform array operations
    def array_operations(self):

        # Ensure data exists before performing operations
        if self.data is not None:
            print("\nGenerating Array Operations.....")

            # Multiply each temperature by 2
            print("\nMultiplying the Dataset:")
            self.multiply_data = self.data * 2
            print(self.multiply_data)

            # Add 5 to each temperature value
            print("\nAdding to the Dataset:")
            self.add_to_data = self.data + 5
            print(self.add_to_data)

            # Reshape the dataset into 2 rows and 4 columns
            print("\nReshaping the Dataset:")
            self.reshape_data = self.data.reshape(2,4)
            print(self.reshape_data)


    # Method to analyze the dataset
    def analyze_data(self):

        # Check if the dataset exists
        if self.data is not None:
            print("\nAnalyzing Dataset.....")

            # Filter temperatures greater than 25 degrees
            print("\nTemperatures above 25 degrees: ")
            self.filter_data = self.data[self.data > 25]
            print(self.filter_data)

            # Perform statistical calculations
            print("\nStatistical Calculations:")

            # Find the minimum temperature
            print("\nMinimum Daily Temperature:")
            self.min_data = self.data.min()
            print(self.min_data)

            # Find the maximum temperature
            print("\nMaximum Daily Temperature:")
            self.max_data = self.data.max()
            print(self.max_data)

            # Calculate the average temperature
            print("\nAverage Daily Temperature:")
            self.avg_data = self.data.mean()
            print(self.avg_data)


# Create an object of the NumericAnalyzer class
analyzer = NumericAnalyzer("Daily Temps")

# Call methods to create and analyze the dataset
analyzer.create_data()
analyzer.array_operations()
analyzer.analyze_data()