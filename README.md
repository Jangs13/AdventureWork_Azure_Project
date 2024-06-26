<div align="center">
  <a href="#">
    <img src="https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/powerBI_1.png" alt="Banner" width="720">
  </a>

  <div id="user-content-toc">
    <ul>
      <summary><h1 style="display: inline-block;">🚀 AdventureWorks Sales Analysis on Azure 🌐</h1></summary>
    </ul>
  </div>
  
  <p>Building a Robust Data Pipeline from On-Premise SQL Server to Azure Cloud: Data Factory, Data Lake Storage, Databricks, Synapse, and PowerBI</p>
</div>
<br>

## 📝 Table of Contents
1. [Project Overview](#introduction)
2. [Key Insights](#key-insights)
3. [Project Architecture](#project-architecture)  
  3.1. [Data Ingestion](#data-ingestion)  
  3.2. [Data Transformation](#data-transformation)  
  3.3. [Data Loading](#data-loading)  
  3.4. [Data Reporting](#data-reporting)
4. [Credits](#credits)
5. [Contact](#contact)

<a name="introduction"></a>
## 🔬 Project Overview 

This project showcases an end-to-end data engineering solution leveraging the power of Azure cloud services. The goal is to migrate and transform data from an on-premise SQL Server to the Azure ecosystem, enabling advanced analytics and interactive reporting with PowerBI. Key components include Azure Data Factory for orchestration, Azure Data Lake for storage, Azure Databricks for data transformation, Azure Synapse Analytics for data warehousing, and PowerBI for data visualization. 

### 💾 Dataset

**AdventureWorks** is a database provided by Microsoft for free on online platforms. It is a product sample database originally published by Microsoft to demonstrate the supposed design of a SQL server database using SQL server 2008. Here are some key points to know about AdventureWorks:

- AdventureWorks database supports a manufacturing MNC named Adventure Works Cycles.
- It is a sample Online Transaction Processing (or OLTP) database, which is a type of data processing where multiple transactions occur concurrently. These are shipped by Microsoft with all of their SQL server products.

> For this project I used the **Lightweight (LT) data**: a lightweight and pared down version of the OLTP sample. [Download here](https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksLT2022.bak)

### 🎯 Project Goals

- Establish a seamless connection between the on-premise SQL Server and Azure cloud services.
- Ingest data from the SQL Server into Azure Data Lake.
- Perform data cleaning and transformation using Azure Databricks and Spark.
- Load the processed data into Azure Synapse Analytics for efficient querying.
- Create dynamic and interactive reports using Microsoft PowerBI.
- Implement robust security and governance using Azure Active Directory (AAD) and Azure Key Vault.

<a name="key-insights"></a>
## 🕵️ Key Insights

- 💸 **Total Revenue by Product Category**
  - *Touring Bikes* is the top 1 category generating revenue with 32% followed by *Road Bikes* with 26% and *Mountain Bikes* with 24%.
 
- 🌍 **Sales by Country**
  - **N°1:** The United Kingdom (UK) have the most total sales with 278 and $572,000 of total revenue.
  - **N°2:** The United States of America (USA) is second with total sales with 264 and $383,810 of total revenue.

- 🚻 **Revenue by Gender**
  - 81% of the revenue is generated by Male customers
  - 19% of the revenue is generated by Female customers  

> This can be explained by males have more interest in doing outdoor activites with the different categories of Bikes than females.

<a name="project-architecture"></a>
## 📝 Project Architecture

The architecture diagram below outlines the end-to-end data pipeline from data ingestion to reporting:

![AzurePipeline-Hamagistral](https://github.com/Hamagistral/Azure-AW/assets/66017329/ebb0f88b-917f-4a6a-be6b-ddf6093ad793)

<a name="data-ingestion"></a>
### 📤 Data Ingestion
-  Integration Runtime: Established a secure connection from on-premise SQL Server to Azure using Microsoft Integration Runtime.

![image](https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/MIR.png)

- Resource Group Setup: Configured necessary Azure services including Key Vault, Storage Account, Data Factory, Databricks, and Synapse Analytics.

![ressource-group](https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/resourcegroup.png)

- Data Migration: Successfully migrated tables from the on-premise SQL Server to Azure Data Lake Storage Gen2.

![image](https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/storageacc.png)
![df-pipeline](https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/synapsepipeline.png)

<a name="data-transformation"></a>
### ⚙️ Data Transformation
- Data Retrieval: Mounted Azure Blob Storage in Databricks to access raw data from the Data Lake.
- Data Processing: Utilized Spark in Azure Databricks to perform data cleaning and transformation tasks.
- Data Storage: Stored the cleaned data in Delta format to optimize performance for subsequent analyses.
![image](https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/Databricks_transformation.png)

<a name="data-loading"></a>
### 📥 Data Loading
- Data Warehousing: Loaded the refined data into Azure Synapse Analytics for efficient querying and reporting.
- Database Connection: Established a connection between Synapse and the data lake to create a robust SQL database.

![synapse-pipeline](https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/synapsepipeline2.png)
![db-synapse](https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/synapsedb.png)

<a name="data-reporting"></a>
### 📊 Data Reporting
- PowerBI Integration: Connected Microsoft PowerBI to Azure Synapse to utilize the processed data.
- Interactive Dashboards: Created insightful and interactive dashboards to visualize key metrics and trends.
![PowerBI-dashboard](https://github.com/Jangs13/AdventureWork_Azure_Project/blob/master/images/powerBI_1.png)

### 🛠️ Technologies Used

- **Data Source**: SQL Server
- **Orchestration**: Azure Data Factory
- **Ingestion**: Azure Data Lake Gen2
- **Storage**: Azure Synapse Analytics
- **Authentication and Secrets Management**: Azure Active Directory and Azure Key Vault
- **Data Visualization**: PowerBI

<a name="credits"></a>
## 📋 Credits

- This Project is inspired by the video of the [YouTube Channel "Mr. K Talks Tech"](https://www.youtube.com/watch?v=iQ41WqhHglk)  

<a name="contact"></a>
## 📨 Contact Me

[LinkedIn](https://www.linkedin.com/in/atharv-jangam/) •
[Gmail](atharvjangam30@gmail.com)
