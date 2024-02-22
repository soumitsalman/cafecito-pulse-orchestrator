import logging
import azure.functions as func
import requests
import config
from icecream import ic
from retry import retry


app = func.FunctionApp()

@app.schedule(schedule=config.get_reddit_collection_schedule(), arg_name="tick", run_on_startup=True,
              use_monitor=False) 
def collect_from_reddit(tick: func.TimerRequest) -> None:
    logging.info("reddit collector triggered")
    # if tick.past_due:
    #     logging.info('The timer is past due!')    
    trigger_collect(config.get_reddit_collector_url())

@retry(Exception, tries=3, delay=30)
def trigger_collect(url: str):
    headers = {"X-API-Key": config.get_internal_auth_token()}
    resp = requests.get(url, headers = headers)
    if resp.status_code == requests.codes["ok"]:
        logging.info(f"collection started: {url}")
        ic(resp.json())
    else:
        error_msg = f"collection failed: {url} | status code: {resp.status_code}"
        logging.error(error_msg)
        raise Exception(error_msg)
        # TODO: throw error