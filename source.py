#!/usr/bin/env python
# coding: utf-8

# # {Cincinnati's "Green Gap" Analysis}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Cincinnati's Distribution of Green Space
# *What problem are you (or your stakeholder) trying to address?*
# Problem: There is an unequal distribution of green space across Cincinnati neighborhoods. While some areas are rich in parks, others—often those with higher population densities or lower income levels—may be "green deserts."
# Importance: Access to green space is linked to better mental health, lower urban temperatures (reducing the "heat island" effect), and higher property values. Understanding this gap allows city planners to prioritize new "green" investments where they are needed most.

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 : "Which Cincinnati neighborhoods have the lowest ratio of park acreage to total neighborhood area, and is there a correlation between neighborhood size and the diversity of park types (Nature Preserves vs. County Parks) available to residents?"
# 

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝  I hypothesize that neighborhood size is not a predictor of green space access. I expect my analysis to reveal that wealthier neighborhoods (like Mt. Lookout or Hyde Park) have a higher ratio of dedicated park acreage and 'nature preserve' types of parks compared to lower-income or more densely populated areas. I also hypothesize that there is a negative correlation between population density and park acreage, meaning that the people who need cooling and outdoor space the most often have the least amount of it

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 I have identified the following three sources to ensure I have a mix of local files and live data:
# 
# File (CSV): Cincinnati_Statistical_Neighborhood_Approximations_2020.csv which I will use to get the official boundaries and total land acreage for each neighborhood.
# 
# File (CSV): Hamilton_County_Parks_and_Greenspace_-_Open_Data.csv which provides me with a complete inventory of all parks, their sizes, and their classifications (e.g., nonprofit vs. government).
# 
# API: The U.S. Census Bureau API, which I will use to pull real-time demographic data, specifically median household income and population totals, for each area.
# I will relate these datasets by using the Neighborhood Name (the SNA_NAME column) as my primary connecting variable.
# First, I will group the Parks data by location and aggregate the total park acreage for each neighborhood.
# Then, I will perform an Inner Join with my Neighborhood CSV using the name of the neighborhood as the key.
# Finally, I will use the Census API to fetch income data for those same neighborhood names and merge that into my master dataframe.
# 

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# My approach is to conduct a geospatial and socio-economic correlation analysis of Cincinnati’s green infrastructure. I will start by quantifying the 'greenness' of each statistical neighborhood using my CSV files. Once I have a baseline of park distribution, I will overlay demographic data from the Census API to look for patterns of inequality.
# 
# My analysis will follow these three stages:
# 
# 1. Data Consolidation: Aggregating all park land within specific neighborhood boundaries.
# 
# 2. Normalization: Converting raw acreage into a percentage (Park-to-Neighborhood ratio) so I can fairly compare large neighborhoods like Westwood to smaller ones like Mt. Adams.
# 
# 3. Statistical Testing: Calculating the correlation coefficient between median income levels and green space accessibility to determine if the 'Green Gap' is statistically significant."
# 
# *How will you use the identified data to answer your project question?*
# 📝 I will use my identified data sources as follows to build a comprehensive answer:
# 
# 1. Neighborhood Data (SNA_NAME, ACRES): I will use this as my primary reference table. The ACRES column is critical because it allows me to calculate the proportion of land that isn't green space, helping me identify 'concrete-heavy' urban areas.
# 
# 2. Parks Data (PARKTYPE, SHAPE__Area): I will use this to categorize the quality of green space. By filtering the PARKTYPE column, I can see if certain neighborhoods only have 'City' playgrounds while others have large 'Nature Preserves.' I will sum the SHAPE__Area of parks within each neighborhood to find the total green footprint.
# 
# 3. Census API Data: I will use the API to pull median household income for each neighborhood. I will then plot this against the green space percentage found in my CSVs.

# In[24]:


# Start your code here
import pandas as pd


try:
    neighborhoods = pd.read_csv('Cincinnati_Statistical_Neighborhood_Approximations_2020.csv')
    parks = pd.read_csv('Hamilton_County_Parks_and_Greenspace_-_Open_Data.csv')

    print("✅ SUCCESS: Data found and loaded from laptop local storage.")
    print(f"Neighborhoods found: {len(neighborhoods)}")
    print(f"Park entries found: {len(parks)}")


    print("\n--- Columns for analysis ---")
    print(f"Neighborhood Columns: {list(neighborhoods.columns)}")
    print(f"Parks Columns: {list(parks.columns)}")

except FileNotFoundError as e:
    print(f"❌ Error: {e}. Make sure the files are in the exact same folder as this script!")


# In[25]:


import matplotlib.pyplot as plt
import seaborn as sns

# Visualization 1: Distribution of Park Sizes (using Matplotlib)
plt.figure(figsize=(10, 6))
plt.hist(parks['SHAPE__Area'], bins=50, color='green', edgecolor='black')
plt.title('Distribution of Park Sizes in Hamilton County')
plt.xlabel('Area (Square Units)')
plt.ylabel('Frequency')
plt.show()


# #Exploratory Data Analysis (EDA)
# 
# Initial Insights
# My EDA focused on the physical footprint of Cincinnati's green infrastructure. I discovered that while Hamilton County has 754 park entries, they are not evenly distributed.
# 
# Distributions: Most parks are small community lots (under 5 acres), but a few "Anchor" parks like Mt. Airy Forest represent the majority of total acreage.
# 
# Correlations: I am investigating the link between a neighborhood's total size (ACRES) and its available park space.
# 
# Issues: The primary issue is a lack of a "Shared Key" between the Neighborhood and Parks datasets, which I addressed in the cleaning section.
# 
# #Visualization Descriptions:
# 
# Park Type Bar Chart: Shows that "Greenspace-Hillside" is the most common type, though these may have lower accessibility than "Nature Preserves."
# 
# Top 10 Parks Bar Chart: Identifies the massive outliers that skew acreage data.
# 
# Neighborhood Histogram: Shows that Cincinnati neighborhoods vary wildly in size, confirming the need for a "Park-to-Land" ratio.
# 
# Linkage Audit: A pie chart showing the percentage of parks successfully matched to neighborhoods via string-matching.
# 
# #The Cleaning Process
# To prepare this data for analysis, I performed the following steps:
# 
# Type Conversion: I encountered a TypeError during string matching; I fixed this by forcing the NAME column to a string type using str() to handle null values.
# 
# Standardization: I converted all neighborhood names and park names to lowercase and stripped whitespace to improve matching accuracy.
# 
# Missing Values: Neighborhoods that did not match any parks were assigned a value of 0 rather than NaN to allow for statistical calculations.
# 
# Anomaly Handling: I identified non-recreational "parks" (like practice fields) that may need to be filtered out in the final stage to avoid bloating the "Greenness" score.
# 
# 
# 

# In[8]:


print("Neighborhoods columns:", neighborhoods.columns.tolist())
print("Parks columns:", parks.columns.tolist())


# In[26]:


# To see if the name of a park contains the neighborhood name
# example: Mount Airy Forest in neighborhood Mount Airy
sample_parks = parks['NAME'].head(20)
sample_neighborhoods = neighborhoods['SNA_NAME'].head(20)

print("Sample Parks:", sample_parks.values)
print("Sample Neighborhoods:", sample_neighborhoods.values)


# In[29]:


#DataCleaning
#1. The "Frequency Audit"
anomalies = ['PRACTICE FIELD', 'MEDIAN', 'SPRING SITE', 'NURSERY']

found_anomalies = parks[parks['NAME'].str.contains('|'.join(anomalies), case=False, na=False)]
print("Sample of Identified Anomalies:")
print(found_anomalies[['NAME', 'PARKTYPE']].head(10))


# Anomaly Handling
# During the cleaning process, I identified several entries that are technically "green" but do not serve the public as recreational parks. Examples include:
# 
# Professional Sports Facilities: Bengals Practice Field.
# Infrastructure/Medians: Chestnut Ridge Median.
# Utility/Administrative Sites:Warder Nursery.
# 
# Action: I have flagged these {is_anomaly.sum()} entries for removal.
# Reasoning: Including these sites would artificially inflate the "Greenness" score of highly urbanized neighborhoods. To accurately measure the "Green Gap," I must focus only on accessible public parks and nature preserves.

# In[31]:


# Clean code
exclude_list = ['PRACTICE FIELD', 'SPRING SITE', 'NURSERY', 'MEDIAN']

parks_cleaned = parks[~parks['NAME'].str.contains('|'.join(exclude_list), case=False, na=False)].copy()
print(f"Rows removed: {len(parks) - len(parks_cleaned)}")
print(f"Remaining parks for analysis: {len(parks_cleaned)}")


# In[34]:


# Data Cleaning 2
parks_cleaned['SNA_NAME'] = parks_cleaned['NAME'].apply(link_neighborhood)
neighborhood_greenery = parks_cleaned.groupby('SNA_NAME')['SHAPE__Area'].sum().reset_index()

neighborhood_greenery.columns = ['SNA_NAME', 'total_park_area']
print(neighborhood_greenery.head())


# In[35]:


# 1. Merge the aggregated park data with your 50 Neighborhoods
final_df = pd.merge(neighborhoods, neighborhood_greenery, on='SNA_NAME', how='left')

# 2. Imputation: Change NaN to 0 for neighborhoods that didn't match a park name
final_df['total_park_area'] = final_df['total_park_area'].fillna(0)

# 3. Calculate the 'Green Ratio' (Park Area divided by Neighborhood Total Area)
final_df['green_ratio'] = final_df['total_park_area'] / final_df['ACRES']

print("--- Top 5 Greenest Neighborhoods (Based on Keyword Matches) ---")
print(final_df[['SNA_NAME', 'green_ratio']].sort_values(by='green_ratio', ascending=False).head())


# Analysis: The Green Space Ratio
# By merging the cleaned park data with the official neighborhood boundaries, I have created a Green Ratio metric. This value represents the percentage of a neighborhood's total acreage that is dedicated to public parks.
# 
# Data Normalization: This step is crucial because comparing raw acreage would unfairly favor large neighborhoods like Westwood. The ratio allows for an apples-to-apples comparison of green access regardless of neighborhood size.
# 
# Current Limitation: Because this is based on string-matching, neighborhoods with zero parks currently listed may actually have parks that were simply not named after the neighborhood (e.g., Eden Park in Walnut Hills). This will be resolved in the final project via Spatial Joining.

# In[36]:


# Data Cleaning 3
parks_cleaned['NAME'] = parks_cleaned['NAME'].str.strip().str.lower()
neighborhoods['SNA_NAME'] = neighborhoods['SNA_NAME'].str.strip().str.lower()
print("Sample of Normalized Park Names:")
print(parks_cleaned['NAME'].head())


# The Issue: The Hamilton County dataset uses inconsistent casing (e.g., "WESTWOOD") compared to the Cincinnati SNA dataset ("Westwood"). Additionally, hidden leading/trailing whitespace ("ghost spaces") can prevent successful joins.
# 
# The Action: I applied .str.strip().str.lower() to the primary key columns in both datasets.
# 
# The Reason: This "Case Folding" technique ensures that string-matching is case-insensitive, significantly increasing the count of successfully linked parks and reducing data fragmentation.

# In[37]:


#Visualization
top_10_green = final_df.sort_values(by='green_ratio', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_10_green, x='SNA_NAME', y='green_ratio', palette='viridis')
plt.title('Top 10 Greenest Neighborhoods (Keyword Match Linkage)')
plt.ylabel('Green Space Ratio')
plt.xticks(rotation=45)
plt.show()


# In[38]:


# Data Cleaning 4
final_df = pd.merge(neighborhoods, neighborhood_greenery, on='SNA_NAME', how='left')

missing_count = final_df['total_park_area'].isna().sum()
print(f"Neighborhoods with no linked parks (NaN): {missing_count}")


# In[39]:


final_df['total_park_area'] = final_df['total_park_area'].fillna(0)
print(f"Neighborhoods with NaN after fix: {final_df['total_park_area'].isna().sum()}")


# The Problem: After performing a left merge between the Neighborhood boundaries and the Linked Parks dataset, neighborhoods that did not have a keyword match in the park names appeared as NaN (Not a Number).
# 
# The Action: I utilized the .fillna(0) method to impute a value of 0 for all missing park acreage entries.
# 
# The Reason: This is a necessary step for Data Integrity. Mathematical operations—specifically the calculation of the Green Space Ratio—cannot be performed on null values. By converting these to zero, I ensure that every neighborhood is represented in the final statistical model.

# In[40]:


#Final Check
final_df['green_ratio'] = final_df['total_park_area'] / final_df['ACRES']
print(final_df[['SNA_NAME', 'total_park_area', 'green_ratio']].head(10))


# #section: Visualization

# In[17]:


#(Matplotlib) Distribution of Park Types
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
parks['PARKTYPE'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Frequency of Park Types in Hamilton County')
plt.ylabel('Count')
plt.show()


# In[18]:


#(Seaborn) Top 10 Largest Parks) 
import seaborn as sns
top_10 = parks.nlargest(10, 'SHAPE__Area')
plt.figure(figsize=(10,6))
sns.barplot(data=top_10, x='SHAPE__Area', y='NAME', palette='viridis')
plt.title('Top 10 Largest Green Spaces by Area')
plt.show()


# In[19]:


#(Matplotlib) Neighborhood Acreage Distribution
plt.figure(figsize=(10,6))
plt.hist(neighborhoods['ACRES'], bins=20, color='orange', alpha=0.7)
plt.title('Distribution of Neighborhood Total Acreage')
plt.xlabel('Acres')
plt.show()


# In[20]:


#(Seaborn) Successful Linkage Audit
plt.figure(figsize=(8,8))
linkage_counts = parks['SNA_NAME'].apply(lambda x: 'Linked' if x != 'Other/Unlinked' else 'Unlinked').value_counts()
plt.pie(linkage_counts, labels=linkage_counts.index, autopct='%1.1f%%', colors=['#66b3ff','#99ff99'])
plt.title('Data Cleaning: Percentage of Parks Linked to Neighborhoods')
plt.show()


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[22]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

