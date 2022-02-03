# Brazilian Election Data Analysis

###### tags: `Tag(change me!)`

Welcome! This repo was created to upload our data analisys project

![](https://i.imgur.com/f5LdxPV.gif)

- Table of Content
[ToC]

## :memo: Project
![](https://media.discordapp.net/attachments/392446181588074501/938595191907029012/unknown.png)
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
The data was handled in a way to minimize and optmize memory and storage, so: 
- Extracting file
- Deleting original zip file
- Creating a list with files path 
- Creating and uploading table to postgreSQL
> It was used only a 10% sample of the data, chosen randomly.

:::info
:bulb: **Tip:** If you want to use the totality of the datasets, then you should use `copy_table` function combined with pandas `.head` method. Once `COPY TABLE` statement require less memory usage. 
:::

---

### Step 3: PostgreSQL :elephant: and Dremio:dolphin:  with Docker :whale: 
 
 **Docker** was used to easy the applications setup.
 
![](https://i.imgur.com/P9MFEG9.png)



 
 **PostgreSQL** was chosen for its open source characteristics.
 
 
 
 And lastly **Dremio** was used as a mid man between **PostgreSQL** and **PowerBI** because of its **PowerBI** integration and interactive analytics directly on the data lake.
 
 ![](https://cdn.discordapp.com/attachments/392446181588074501/938576123892203620/1wmFlv2ccJ9Z3u3tYP_7r4A.png)
---
