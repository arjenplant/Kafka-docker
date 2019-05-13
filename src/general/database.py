from pony.orm import Database, PrimaryKey, Required, db_session, count, Optional
from general import env_vars
import logging as log
from datetime import datetime

db = Database()

log.basicConfig(level=log.INFO)


def init_db() -> Database:
    if db.provider is None:
        log.info("Initialising connection to postgress")
        db.bind(
            provider="postgres",
            user=env_vars.POSTGRES_USER,
            password=env_vars.POSTGRES_PASSWORD,
            host=env_vars.POSTGRES_HOST,
            database=env_vars.POSTGRES_DATABASE,
        )
        db.generate_mapping(create_tables=True)
    # db.drop_all_tables(with_all_data=True) # USE TO CLEAR DB ON ONLY FOR DEVELOPMENT!!!!
   

class Article(db.Entity):
    article_id = PrimaryKey(str)
    article_section = Required(str)
    article_type = Required(str)
    article_publication_date = Required(datetime)
    article_title = Required(str)
    article_url = Optional(str)


@db_session
def insert_data(
    article_id: str,
    article_section: str,
    article_type: str,
    article_publication_date: datetime,
    article_title: str,
    article_url: str):
    if not Article.exists(article_id=article_id):
        Article(
            article_id = article_id,
            article_section = article_section,
            article_type = article_type,
            article_publication_date = article_publication_date,
            article_title = article_title,
            article_url = article_url,
        )
        return 1
    return 0

@db_session
def collect_all_articles():
    return Article.select().show(width=200)


@db_session
def exist(article_id):
    return Article.exists(article_id=article_id)


@db_session
def collect_specific_event(article_id):
    return Article[article_id]


@db_session
def get_row_count(entity: db.Entity):
    return count(e for e in entity)

if __name__ == "__main__":
    db = init_db()
    print(get_row_count(Article))
    collect_all_articles()
