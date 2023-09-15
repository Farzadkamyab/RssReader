## Project Description

This project aims to develop an RSS feed aggregator using Django. The aggregator will extract and store data from various RSS feed sources, including APIs and custom XML feeds. It will implement advanced parsing techniques, data mapping, and flexible schema design to accommodate diverse feed structures. The project will also include custom JWT authentication using Redis to store access tokens and utilize and PostgreSQL as the database.

Follow these steps to set up the project locally:

1. 👉 Clone the repository:

   ```bash
   git clone https://github.com/Farzadkamyab/RssReader.git
   ```

2. 👉 Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. 👉 Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. 👉 Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. 👉 Run migrations to create the database schema:

   ```bash
   python manage.py migrate
   ```

6. 👉 Start the Django development server:

   ```bash
   python manage.py runserver
   ```

The project should now be running locally at `http://localhost:8000/`.✅


## Usage of Project

To use these endpoints, you can make GET and POST requests to the URLs listed above as per your requirements. For example:

- To parse and save rss file to database automatically, make a POST request with "xml" key and send your rss file to `podcast/import/`
- To list all podcasts, make a GET request to `/podcast/podcasts`.
- To retrieve details of a specific podcast with ID 1, make a GET request to `podcast/podcast/1/`.
- To list all episodes, make a GET request to `/podcast/episodes/`.
- To retrieve details of a specific episode with ID 1, make a GET request to `podcast/episode/1/`.-
