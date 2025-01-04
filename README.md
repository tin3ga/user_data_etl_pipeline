<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">user data etl pipeline</h3>

  <p align="center">
    An ETL pipeline that extracts user data from a public API, transforms the data into a clean, analyzable format, and loads it into a PostgreSQL database
    <br />
    <a href="https://github.com/tin3ga/user_data_etl_pipeline"><strong>Explore the docs »</strong></a>
    <br />
    <br />
   
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#structure">Structure</a></li>
      </ul>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

### Structure

```
.
├── src/
│   ├── config.py         # Configuration for URL files, database credentials
│   ├── extract.py        # Code for extracting data from APIs
│   ├── transform.py      # Code for cleaning and transforming the data
│   ├── load.py           # Code for loading data into PostgreSQL
│   └── utils.py          # Utility functions for the ETL process
├── poetry.lock
├── pyproject.toml
├── README.md             # Project documentation
├── LICENSE               # License details
└── run.sh                # Executable for ETL

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- **Programming Language:** Python
- **Database:** PostgreSQL
- **Data Sources:**

  - **DummyJson API:** [DummyJson](https://dummyjson.com/users)

- **Python Libraries:**
  - `requests`: For interacting with APIs.
  - `pandas`: For data manipulation and cleaning.
  - `SQLAlchemy`: For database interaction.
  - `numpy`: For numerical computations.
  - `dotenv`: To handle environment variables (API keys, DB credentials).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/tin3ga/user_data_etl_pipeline.git
   ```
2. Create and activate a virtual environment:

```bash
python3 -m `venv` venv
source `venv`/bin/activate  # On Windows: `venv`\Scripts\activate
```

3. Set up the environment variables:
   - Create a `.env` file in the root directory with the following keys:
     ```
     DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<`dbname`>
     ```
4. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin tin3ga/user_data_etl_pipeline
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Run the ETL pipeline:

Make file executable

```bash
chmod +x run.sh
```

Execute the script with

```bash
./run.sh
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
