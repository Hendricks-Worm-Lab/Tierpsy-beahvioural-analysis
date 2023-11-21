import h5py
import pandas as pd
import os

def csv_export(input_path, output_path):
    # Open the HDF5 file
    with h5py.File(input_path, 'r') as f:
        # Extract the data table called trajectories_data
        data = f['trajectories_data'][:]
    
    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame as a CSV file
    df.to_csv(output_path, index=False)

# Example usage
input_dir = r"D:\Tierpsy_analysis\Rhomboid_FINALE\interpolated\Results"
output_dir = r"D:\Tierpsy_analysis\Rhomboid_FINALE\interpolated\Results\CSV"
for filename in os.listdir(input_dir):
    if filename.endswith("_featuresN.hdf5"):
        input_path = os.path.join(input_dir, filename)
        name, extension = os.path.splitext(filename)
        output_path = os.path.join(output_dir, name + '.csv')
        print(filename +" being exported!")
        csv_export(input_path, output_path)
        print("done!")