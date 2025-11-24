# PandasAI 101 - Project Navigation

This document will help you navigate the structure of the PandasAI training project.

## 📚 Project Structure

### 1. Foundations - `1_foundations/`

Introduction to working with PandasAI. Basic examples of library usage.

- **[1_chat.ipynb](1_foundations/1_chat.ipynb)** - Basics of working with `chat()` method for DataFrame
- **[2_csv.ipynb](1_foundations/2_csv.ipynb)** - Working with CSV files
- **[3_chat_multi_sources.ipynb](1_foundations/3_chat_multi_sources.ipynb)** - Working with multiple data sources

### 2. Agent - `2_agent/`

Learning to work with agents in PandasAI - a more advanced way to interact with data.

- **[01_agent.ipynb](2_agent/01_agent.ipynb)** - Basic agent usage example
- **[02_skills.ipynb](2_agent/02_skills.ipynb)** - Creating and using custom skills
- **[03_agent_follow_up_example.ipynb](2_agent/03_agent_follow_up_example.ipynb)** - Examples of follow-up requests to the agent
- **[04_agent_prompt.ipynb](2_agent/04_agent_prompt.ipynb)** - Working with prompts for agents
- **exports/** - Exported charts and results

### 3. Visualisation - `3_visualisation/`

Creating charts and visualizations using PandasAI.

- **[01_plot_example.ipynb](3_visualisation/01_plot_example.ipynb)** - Chart creation examples
- **exports/** - Exported visualizations

### 4. Semantic - `4_semantic/`

Working with PandasAI semantic functions to create and load datasets.

- **[01_pai_create.ipynb](4_semantic/01_pai_create.ipynb)** - Creating datasets using `pai.create()`
- **[02_pai_load.ipynb](4_semantic/02_pai_load.ipynb)** - Loading datasets using `pai.load()`
- **[03_pai_create_large.ipynb](4_semantic/03_pai_create_large.ipynb)** - Creating large datasets
- **[04_pai_create_group.ipynb](4_semantic/04_pai_create_group.ipynb)** - Creating grouped datasets
- **sales.csv** - Sample data for work

### 5. Advanced - `5_advanced/`

Advanced features and integrations of PandasAI.

- **[01_verbose.ipynb](5_advanced/01_verbose.ipynb)** - Verbose mode for debugging
- **[02_verbose agent.ipynb](5_advanced/02_verbose%20agent.ipynb)** - Verbose mode for agents
- **[03_factor_analyze.ipynb](5_advanced/03_factor_analyze.ipynb)** - Factor analysis of data
- **[04_postgresql_connector.ipynb](5_advanced/04_postgresql_connector.ipynb)** - Integration with PostgreSQL
- **generate_data.py** - Script for generating test data
- **psychometric_data.csv** - Psychometric data for analysis

### 6. Train (Training and Vector DBs) - `6_train/`

Training agents and working with vector databases.

- **[01_train.ipynb](6_train/01_train.ipynb)** - Training an agent on examples
- **[02_lancedb.ipynb](6_train/02_lancedb.ipynb)** - Integration with LanceDB
- **[03_qdrant.ipynb](6_train/03_qdrant.ipynb)** - Integration with Qdrant
- **lancedb/** - LanceDB Data (Vector Indexes)
- **vector_cache/** - Vector Data Cache (ChromaDB)

### 7. Sandbox - `7_sandbox/`

Experimental folder for testing and experiments.

*Folder is empty - use for your experiments*

### 8. Others - `8_others/`

Additional examples and comparisons.

- **[duck vs vector.ipynb](8_others/duck%20vs%20vector.ipynb)** - Comparison of DuckDB and vector DBs

---

## 🚀 Recommended Learning Order

1. **Start with basics** (`1_foundations/`) - learn basic PandasAI capabilities
2. **Move to agents** (`2_agent/`) - learn to work with agents and skills
3. **Learn visualization** (`3_visualisation/`) - create charts
4. **Master semantic operations** (`4_semantic/`) - working with datasets
5. **Explore advanced topics** (`5_advanced/`) - integrations and debugging
6. **Learn training** (`6_train/`) - training agents and vector DBs

## 📝 Notes

- All notebooks use PandasAI v3.0.0+
- OpenAI API key (or other LLM provider) is required
- It is recommended to use environment variables to store API keys
- Some examples require additional dependencies (PostgreSQL, LanceDB, Qdrant)

## 🔗 Useful Links

- [PandasAI Documentation](https://docs.pandas-ai.com/)
- [PandasAI GitHub](https://github.com/gventuri/pandas-ai)

---

*Last updated: 2025*

