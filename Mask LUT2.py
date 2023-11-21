from PIL import Image
import numpy as np
import pandas as pd
import os

def stack_x_axis(input_path, output_path):
    # Open the image and convert to a NumPy array
    img = Image.open(input_path)
    img_arr = np.asarray(img)

    # Create arrays of X and Y values
    x = np.arange(1, 4001)
    y = np.arange(1, 4001)

    # Use numpy.where() to create a lookup table
    lookup_table = np.column_stack((np.repeat(y, 4000), np.tile(x, 4000), img_arr.reshape(-1, 1)))

    print(lookup_table)

    # Convert the NumPy array to a Pandas DataFrame
    df = pd.DataFrame(lookup_table, columns=['Y','X','DATA'])

    # Save the result as a CSV file
    df.to_csv(output_path, index=False)

    return df

# Example usage
input_dir = r"D:\Tierpsy_analysis\Rhomboid_FINALE\interpolated\Masks\Resized"
output_dir = r"D:\Tierpsy_analysis\Rhomboid_FINALE\interpolated\Masks\Resized\stacked"
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        input_path = os.path.join(input_dir, filename)
        name, extension = os.path.splitext(filename)
        output_path = os.path.join(output_dir, name + '.csv')
        print(filename +" being exported!")
        stack_x_axis(input_path, output_path)
        print("done!")