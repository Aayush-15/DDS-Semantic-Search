from elasticsearch import Elasticsearch
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic","OOcrmca+WaJCZkPWN1i_"),
    verify_certs=False
)
print(es.ping())
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-mpnet-base-v2')
import pandas as pd
from indexMapping import indexMapping
df = pd.read_csv("myntra_products_catalog.csv").loc[:499]
df.head()

df.isna().value_counts()
df.fillna("None", inplace=True)

df["DescriptionVector"] = df["Description"].apply(lambda x: model.encode(x))
print(df.head())

es.indices.create(index="all_products", mappings=indexMapping)

record_list = df.to_dict("records")
for record in record_list:
    try:
        es.index(index="all_products", document=record, id=record["ProductID"])
    except Exception as e:
        print(e)

print(es.count(index="all_products"))


input_keyword = "Blue Shoes"
vector_of_input_keyword = model.encode(input_keyword)

query = {
    "field" : "DescriptionVector",
    "query_vector" : vector_of_input_keyword,
    "k" : 2,
    "num_candidates" : 500, 
}

res = es.knn_search(index="all_products", knn=query , source=["ProductName","Description"])
res["hits"]["hits"]
print(res["hits"]["hits"])