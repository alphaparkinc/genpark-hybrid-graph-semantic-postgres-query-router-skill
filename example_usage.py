from client import HybridGraphSemanticPostgresQueryRouterClient

def main():
    client = HybridGraphSemanticPostgresQueryRouterClient()
    res = client.route_query("Find FinTech companies with ARR over $1M that are using LangChain")
    print(f"Query Type: {res['query_type_used']}")
    print("Query Plan:", res["query_plan"])
    print("Results:")
    for row in res["result_rows"]:
        print(f"  {row['company']} — ARR ${row['arr_usd']:,} | Similarity: {row['similarity_score']}")

if __name__ == "__main__":
    main()
