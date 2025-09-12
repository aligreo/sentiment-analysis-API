# Sentiment Analysis API using FastAPI Framework

![Sentiment Analysis Demo](https://via.placeholder.com/800x400.png?text=Sentiment+Analysis+UI)

**Note:** Replace the placeholder image above with a screenshot of the actual UI.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
```markdown
# Sentiment Analysis API using FastAPI

![Sentiment Analysis Demo](https://via.placeholder.com/900x360.png?text=Sentiment+Analysis+UI)

## What's Changed (UI & Templates)

- Modern, responsive UI using an external stylesheet at `src/static/css/main.css`.
- Introduced a `base.html` template and consistent page layouts for `index`, `generate`, and `history` pages.
- Clean typography (Google Inter), refined color palette, and improved spacing for readability.
- Polished controls: improved primary button with a loading spinner and accessible focus states.
- Result cards styled with clear positive/negative/neutral variants and better contrast.
- `generate` page renders model output as Markdown (server-side parsed to HTML) and displays it safely.
- Responsive breakpoints added for mobile and tablet; layout is optimized for small screens.

These improvements were implemented by updating `src/static/css/main.css` and the templates in `src/templates/`.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sentiment-analysis-API
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv sa
# Windows (PowerShell)
sa\Scripts\Activate.ps1
# Windows (cmd)
sa\Scripts\activate.bat
# Unix / macOS
source sa/bin/activate
```

3. Install dependencies:
```bash
pip install -r src/requirements.txt
```

### Configuration

1. Create a `.env` file inside `src/` if required and update any settings (e.g. `OPENROUTER_API_KEY`, database credentials).
2. If using MySQL, ensure the correct driver is installed (e.g. `mysql-connector-python`) and update `src/models/db.py` with your credentials.

### Running the Application

```bash
cd src
uvicorn main:app --reload
```

Open `http://localhost:8000` to view the UI.

## API Endpoints (summary)

- `GET /` - Web interface (index page)
- `POST /` - Form submission for sentiment analysis (index)
- `GET /generate` - Text generation UI page
- `POST /generate` - Generate text (renders Markdown output)
- `GET /history` - History/previous outputs page

## Notes on Models

- Sentiment models use Hugging Face `transformers` by default. Update `model_name` in configuration to switch models.
- For text generation via OpenRouter (or other LLM providers), ensure you set the appropriate API keys in environment/config.

---
If you'd like, I can also add a screenshot and a short demo GIF to the README. Would you like me to add that next?
```