import os

def get_reddit_collector_url() -> str:
    return os.getenv("REDDIT_COLLECTOR_URL")+"/collect"

def get_internal_auth_token() -> str:
    return os.getenv("INTERNAL_AUTH_TOKEN")

def get_reddit_collection_schedule() -> str:
    return os.getenv("REDDIT_COLLECTION_SCHEDULE")