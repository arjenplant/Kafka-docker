from setuptools import setup, find_packages 

setup(
    name="news_streaming",
    version="0.1.0",
    package_dir={"": "src"},  # add this is you use the src layout
    packages=find_packages("src"),
    setup_requires=[
        "pytest-runner", 
        "flake8",
        ],
    install_requires=[
        "wheel",
        "pyhocon", # For the configuration files
        "kafka-python",  # For interaction with Kafka
        "requests",  # for making the API call
        "toolz",  # for creating pipelines
        "pony",  # Databse ORM https://docs.ponyorm.org
        "psycopg2-binary",  # Binary since the normal one doesnt work
        ],  
    extras_require={"dev": [  # optional [dev] for dev enviroments
        "pytest",
        "mypy",
        "flake8",
        "black",
        ],
        "interactive": [  # Optional interactive mode if want to work with jupyter notebook
            "jupyter"
        ],
        },
    tests_require=[
        "pytest"
        ],
)
