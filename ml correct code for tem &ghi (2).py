import sklearn
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta
import time
# Load the dataset
file_path = "D:/niteditedfinal.csv"

# Load the dataset
data = pd.read_csv(file_path)

while True:

    # Split data into features (X) and targets (y_temp, y_ghi)
    X = data[[ 'Year' , 'Month','Day','Hour','Minute']]
    y_temp = data['Temperature']  # predict Temperature
    y_ghi = data['GHI']  # predict GHI

    # Split data into training and testing sets
    X_train, X_test, y_train_temp, y_test_temp = train_test_split(X, y_temp, test_size=0.2, random_state=42)
    X_train, X_test, y_train_ghi, y_test_ghi = train_test_split(X, y_ghi, test_size=0.2, random_state=42)

    # Train the random forest regressor models
    rf_temp = RandomForestRegressor()
    rf_temp.fit(X_train, y_train_temp)

    rf_ghi = RandomForestRegressor()
    rf_ghi.fit(X_train, y_train_ghi)

    # Get the current time (IST)
    current_time = datetime.now() #+ timedelta(hours=5.5)  # IST is 5 hours 30 minutes ahead of UTC

    # Extract hour and minute components from the datetime object
    hour = current_time.hour
    minute = current_time.minute
    year = current_time.year
    month = current_time.month
    day = current_time.day

    # Create a new input array with the current values
    X_new = np.array([[hour, minute,year,month,day]])  # assuming hour and minute are the input features

    # Make a single prediction
    prediction_temp = rf_temp.predict(X_new)
    prediction_ghi = rf_ghi.predict(X_new)

    print("Predicted Temperature:", prediction_temp[:])
    print("Predicted GHI:", prediction_ghi[:])

    # Predict for the next 15 minutes
    #for i in range(15):
    
    current_time += timedelta(minutes=15)
    print(current_time)
    hour = current_time.hour
    minute = current_time.minute
    year = current_time.year
    month = current_time.month
    day = current_time.day
    X_new = np.array([[hour, minute,year,month,day]])
    prediction_temp = rf_temp.predict(X_new)
    prediction_ghi = rf_ghi.predict(X_new)
    print(f"Predicted Temperature in {i+1} minutes:", prediction_temp[0])
    print(f"Predicted GHI in {i+1} minutes:", prediction_ghi[0])

    # Add a delay before the next iteration
   # time.sleep(15 * 60)
