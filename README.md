# Brazilian Election Data Analysis

Welcome! This repo was created to upload our data analisys project.

![](https://i.imgur.com/f5LdxPV.gif)

## :memo: Project Summary

This project had the intention of covering all steps of an **ELT** data integration, from extraction, passing through a creation of a data lake, uploaded to a database (data warehouse) and being transformed for data visualization.

![](https://cdn.discordapp.com/attachments/392446181588074501/938933559081717761/unknown.png)
### Step 1: Data Acquisition

The data was acquired through the [TSE](https://dadosabertos.tse.jus.br/) (Brazilian Superior Electoral Court) repository.

To do so, it was used [scrapy](https://scrapy.org/) library to create a crawler that look up for **HTML** tags and download the correspondent files.
``` Python
file_url = response.css('.resource-url-analytics::attr(href)').get()
```

---

### Step 2: Handling Data

Using the following **Python** libraries:

``` Python
import os
import csv 
import pandas
import random
import zipfile
import pathlib
import sqlalchemy
```
The data was handled in a way to minimize and optmize memory and storage, so the steps were the following:
- Extracting file
- Deleting original zip file
- Creating a list with files path 
- Creating and uploading table to postgreSQL
> It was used only a 10% sample of the data, chosen randomly.

:bulb: **Tip:** If you want to use the totality of the datasets, then you should use `copy_table` function combined with pandas `.head` method. Once `COPY TABLE` statement require less memory usage. 

---

### Step 3: PostgreSQL :elephant: and Dremio:dolphin:  with Docker :whale: 
 
 **Docker** was used to easy the applications setup by creating containers as shown on the diagram:
 <p align="center">
  <img src="https://i.imgur.com/P9MFEG9.png" />
</p>


 
 **PostgreSQL** was chosen for its open source characteristics and easy conection to **Dremio**.
 
 

 And lastly **Dremio** was used as a mid man between **PostgreSQL** and **PowerBI** because of its **PowerBI** integration and interactive analytics directly on the data lake.
 <p align="center">
  <img src="https://cdn.discordapp.com/attachments/392446181588074501/938922380280070154/unknown.png" />
</p>
 
 
---

### Step 4: Setting up Dremio's Virtual Datesets
**Dremio** was mainly used to create virtual datasets, known as views in a **SQL** database. A series of **SQL** queries were made to format data type, remove the missing values from the data source and direct connecting those views to **PowerBI**.
```sql
Select 
    Cast(Replace("ANO_ELEICAO", '"', '') AS varchar(100)) AS "ANO_ELEICAO",
    Cast(Replace("SG_UF", '"', '') AS varchar(100)) AS "SG_UF",
    Cast(Replace("CD_MUNICIPIO", '"', '') AS varchar(100)) AS "CD_MUNICIPIO",
    Cast(Replace("NM_MUNICIPIO", '"', '') AS varchar(100)) AS "NM_MUNICIPIO",
    Cast(Replace("CD_GENERO", '"', '') AS varchar(100)) AS "CD_GENERO",
    Cast(Replace("DS_GENERO", '"', '') AS varchar(100)) AS "DS_GENERO",
    Cast(Replace("QT_ELEITORES_PERFIL", '"', '') AS bigint) AS "QT_ELEITORES_PERFIL",
    Cast(Replace("QT_ELEITORES_BIOMETRIA", '"', '') AS bigint) AS "QT_ELEITORES_BIOMETRIA",
    Cast(Replace("QT_ELEITORES_DEFICIENCIA", '"', '') AS bigint) AS "QT_ELEITORES_DEFICIENCIA",
    Cast(Replace("QT_ELEITORES_INC_NM_SOCIAL", '"', '') AS bigint) AS "QT_ELEITORES_INC_NM_SOCIAL"
From "perfil_eleitorado_1994.csv"
```
Prior to the formatting queries, a verification of the columns was done:

```sql
Select 
CASE 
WHEN (Select COUNT("CD_MUN_SIT_BIOMETRICA") 
        FROM "perfil_eleitorado_1994.csv"
        Where "CD_MUN_SIT_BIOMETRICA" = '-3') = COUNT("CD_MUN_SIT_BIOMETRICA") THEN TRUE
ELSE FALSE
END AS "CD_MUN_SIT_BIOMETRICA", 
CASE
WHEN (Select COUNT("NR_ZONA") 
        FROM "perfil_eleitorado_1994.csv"
        Where "NR_ZONA" = '-1') = COUNT("NR_ZONA") THEN TRUE
ELSE FALSE
END AS "NR_ZONA",
CASE
WHEN (Select COUNT("CD_ESTADO_CIVIL") 
        FROM "perfil_eleitorado_1994.csv"
        Where "CD_ESTADO_CIVIL" = '-3') = COUNT("CD_ESTADO_CIVIL") THEN TRUE
ELSE FALSE
END AS "CD_ESTADO_CIVIL",
CASE
WHEN (Select COUNT("CD_FAIXA_ETARIA") 
        FROM "perfil_eleitorado_1994.csv"
        Where "CD_FAIXA_ETARIA" = '-3') = COUNT("CD_FAIXA_ETARIA") THEN TRUE 
ELSE FALSE
END AS "CD_FAIXA_ETARIA",
CASE
WHEN (Select COUNT("CD_GRAU_ESCOLARIDADE") 
        FROM "perfil_eleitorado_1994.csv"
        Where "CD_GRAU_ESCOLARIDADE" = '0') = COUNT("CD_GRAU_ESCOLARIDADE") THEN TRUE
ELSE FALSE 
END AS "CD_GRAU_ESCOLARIDADE"
FROM "perfil_eleitorado_1994.csv"
```
---

### Step 5: Data Visualization with PowerBI

**PowerBI** is a widely used collection of software services, easy to use and with a self-service approach to Business Inteligence. 
The data visualization of this project was made with **PowerBI**. 

As an example the following images are some of the graphics created with **PowerBI**

![](https://cdn.discordapp.com/attachments/392446181588074501/938924658307248139/unknown.png)

<p align="center">
<img src="https://cdn.discordapp.com/attachments/392446181588074501/938932692853067796/unknown.png" width="406"/> <img src="https://cdn.discordapp.com/attachments/392446181588074501/938932132275970128/unknown.png" width="420"/> 

---

### :arrow_down:  If you want to access the full project file you can download it [here](https://drive.google.com/drive/folders/1CcHrlOj5TVn5fHvQXzWT9zUapLhuVTeQ?usp=sharing)
