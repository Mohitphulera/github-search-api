# GitHub Search API with Caching

This Django application provides a RESTful API to search GitHub for users, repositories & issues and caches the results using Redis for optimized repeated queries.

## Features

- Search GitHub for users, repositories, or issues.
- Results are cached in Redis for 2 hours to minimize redundant external API calls.
- An API endpoint to clear the backend cache.
- Unit tests to ensure robustness and reliability.
- Swagger documentation for easy API reference and testing.

## Installation & Dependencies

Before you begin using the application, you need to install the necessary dependencies to ensure everything runs smoothly.

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Redis server

### Setting Up & Installing Dependencies

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Mohitphulera/github-search-api.git
   cd github-search-api

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

4. **Run Migrations**

   ```bash
   python manage.py migrate

5. **Run the Development Server**

   ```bash
   python manage.py runserver


## Usage

Using the GitHub Search API with caching is straightforward. Here are the main API endpoints and how to utilize them:

1. **Search GitHub**:
   - **Endpoint**: `/github/api/search/`
   - **Method**: `POST`
   - **Payload**:
     ```json
     {
       "search_type": "users",  // Options: 'users', 'repositories', or 'issues'
       "search_text": "your_query_here"
     }
     ```
   Use this endpoint to search GitHub for users, repositories, or issues. The results will be cached for 2 hours.

2. **Clear Cache**:
   - **Endpoint**: `/github/api/clear-cache/`
   - **Method**: `POST`
   
   If you want to manually clear the cached results, use this endpoint.

3. **Swagger Documentation**:
   - **Access Point**: `/swagger/`

   For a detailed description of the API endpoints, their expected inputs, and outputs, visit the Swagger documentation page at `/swagger/` on your hosted application.
   ![image](https://github.com/Mohitphulera/github-search-api/assets/30733552/e1ae0eff-763b-4e01-afb1-765b9ac77901)


## Running Tests

To ensure the application works as expected, run:

```bash
python manage.py test

