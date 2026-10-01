import pandas as pd
import yaml as yml
import json

calibration = pd.read_csv("calibrations.csv")
sensor = pd.read_excel("sensors.xlsx")

with open("config.yml", "r") as file:
    data = yml.safe_load(file)

#df = pd.DataFrame(data)

max_days = data["max_days_since_calibration"]
output_file = data["output_file"]

calibration_data= calibration[calibration["days_since_calibration"] > max_days]

join_data = pd.merge(sensor, calibration_data, on="sensor_id", how="inner")
print(join_data.columns.tolist())

result = join_data[["sensor_id", "lab_room","owner", "days_since_calibration"]]

with open(output_file, "w") as f:
    json.dump(result.to_dict(orient="records"), f, indent = 2)







