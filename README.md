Run these commands from the project folder to reproduce experiments:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export OPENAI_API_KEY="your-api-key"

python 0_train_models.py
python 1_basic_mcp.py
python 2_llm_mcp.py
```