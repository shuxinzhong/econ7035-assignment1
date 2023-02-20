import pandas as pd
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('contact_info_file', help='Contact info file(CSV)')
parser.add_argument('other_info_file', help='Other info file(CSV)')
parser.add_argument('output_file', help='Cleaned data file(CSV)')

args = parser.parse_args()


# (1)
contact_df = pd.read_csv(args.contact_info_file)
other_df = pd.read_csv(args.other_info_file)
merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id').drop('id', axis=1)

# (2)
merged_df.dropna(inplace=True)

# (3)
merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

# (4)
merged_df.to_csv(args.output_file, index=False)

# Step 3
print(merged_df)
print("Output file shape:")
print(merged_df.shape)