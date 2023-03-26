
# monitoring.py
# ...
def save_to_database(input: Item, result: Result) -> None:
    """
    Saves input/output dicts to bigquery
    """
    client = BigQuery.client()  # Of any other SQL/Permanent data storage
    table = "your_cool_bq_table"
    current_time = datetime.datetime.now()

    rows_to_insert = [(current_time, input.json(), result.json())]
    errors = client.insert_rows(table, 
                                rows_to_insert)

    if errors:
        logging.info(f"Error: {str(errors)}")
        return 

    logging.info("Saved prediction")


# app.py
# ...
from fastapi import FastAPI, BackgroundTasks
from .monitoring import save_to_database
# ...

# create an endpoint that receives POST requests
@app.post("/predict/", 
          reponse_model=Result, 
          background_tasks: BackgroundTasks)
def predict(features: Item):
    # some processing
    prediction = get_prediction_for(features)
    background_tasks.add_task(save_to_database, input=features, result=prediction)
    return prediction