
# RAG-Based Support Ticket System

This project implements a **Retrieval-Augmented Generation (RAG)** model for handling support tickets. It uses **semantic search** and **generative AI** to find relevant past tickets and generate helpful responses based on user queries.

## Features

* **Semantic Search**: Retrieves relevant support tickets using sentence embeddings and FAISS for fast similarity search.
* **Generative AI**: Uses Gemini (Google's generative model) to generate helpful responses based on the retrieved tickets.
* **Feedback Mechanism**: Allows users to provide feedback on the generated responses to improve system quality.

## Requirements

* **Python 3.x**
* **Libraries**:

  * `sentence-transformers`
  * `faiss-cpu`
  * `google-generativeai`
  * `numpy`
  * `python-dotenv`
  * `json`

You can install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Setup

### 1. **Clone the Repository**

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/rag-support-ticket-system.git
cd rag-support-ticket-system
```

### 2. **API Key Setup**

This project uses **Gemini API** for generating support responses. To use the Gemini API, you need to add your API key to a `.env` file.

Create a `.env` file in the root directory and add your `GEMINI_API_KEY`:

```bash
GEMINI_API_KEY=your-gemini-api-key
```

You can obtain your API key from [Google Gemini](https://cloud.google.com/generative-ai).

### 3. **Ticket Data**

Ensure that the `data/tickets.json` file is present, containing the support ticket data. A sample format is provided below:

```json
[
  {
    "id": 1,
    "title": "Login failure on Safari for SSO users",
    "browser": "Safari 16.3",
    "os": "macOS Ventura",
    "customer_type": "Enterprise",
    "issue": "Redirect loop during SSO login",
    "resolution": "Clear cookies, update Safari settings to allow cross-site tracking."
  },
  {
    "id": 2,
    "title": "Generic login issues",
    "browser": "All",
    "customer_type": "Mixed",
    "issue": "Password reset email not received",
    "resolution": "Whitelist support domain in email settings."
  }
]
```

### 4. **Running the Application**

Once you have set up the `.env` file and the ticket data, you can start the application.

Run the following command:

```bash
python main.py
```

This will launch an interactive terminal where you can enter support queries. The system will search for relevant tickets and generate responses based on the retrieved tickets.

### 5. **Feedback Collection**

After receiving a response, you can provide feedback by typing `y` or `n`. The feedback will be saved in `feedback_log.txt`.

## File Structure

* **`main.py`**: Entry point for the application.
* **`generator.py`**: Handles the response generation using the Gemini API.
* **`retriever.py`**: Manages ticket loading, indexing, and searching using FAISS and sentence embeddings.
* **`data/tickets.json`**: Contains the support ticket data.
* **`feedback_log.txt`**: Stores user feedback on generated responses.
* **`.env`**: Holds sensitive environment variables like the Gemini API key.
* **`requirements.txt`**: Lists the Python dependencies required for the project.

## How It Works

1. **Load Tickets**: The `load_tickets` function loads the support tickets from a JSON file.
2. **Build Index**: The `build_index` function uses sentence embeddings to convert the ticket data into numerical vectors. These vectors are indexed using FAISS for efficient search.
3. **Search Tickets**: The `search_tickets` function finds the top-k most relevant tickets based on the user's query.
4. **Generate Response**: The `generate_response` function uses the Gemini generative model to create a response based on the search results.
5. **Feedback Mechanism**: Users can provide feedback on the responses, which is logged for further improvement.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please ensure that your code follows the style and functionality described above.

