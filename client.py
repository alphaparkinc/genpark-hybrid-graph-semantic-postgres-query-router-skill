class HybridGraphSemanticPostgresQueryRouterClient:
    def route_query(self, natural_language_query: str, schema_context: dict = None) -> dict:
        return {
            "query_plan": {
                "tabular_filter": "WHERE industry = 'FinTech' AND arr_usd > 1000000",
                "graph_traversal": "MATCH (c:Company)-[:USES]->(t:Technology {name: 'LangChain'})",
                "semantic_search": "COSINE_SIMILARITY(company_description_embedding, query_embedding) > 0.87"
            },
            "result_rows": [
                {"company": "Neuron Analytics", "arr_usd": 4200000, "uses_langchain": True, "similarity_score": 0.93},
                {"company": "Flux Labs AI", "arr_usd": 2800000, "uses_langchain": True, "similarity_score": 0.89}
            ],
            "query_type_used": "HYBRID_TABULAR_GRAPH_SEMANTIC"
        }
