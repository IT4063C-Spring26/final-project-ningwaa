#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
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

# 

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

# In[7]:


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


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[8]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

