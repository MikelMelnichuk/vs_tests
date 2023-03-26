# From:

# ... rest of the monitoring.py

# this function generates a dashboard from our reference and prediction data
# which is then saved to a `drift.html` file
def generate_dashboard() -> str:
    dasboard_name = "static/drift.html"
    data_drift_dashboard = Dashboard(
        tabs=[
            DataDriftTab(verbose_level=0),
        ]
    )

    reference_data = load_reference_data()
    current_data = load_last_predictions()

    data_drift_dashboard.calculate(
        reference_data=reference_data,
        current_data=current_data,
        column_mapping=None,
    )

    data_drift_dashboard.save(dasboard_name)
    logger.info(f"Dashboard saved to {dasboard_name}")
    return dasboard_name


# -------------------------------------------------------
# Notice how we’re creating our dashboard, and then saving it to a static/drift.html file.
#   The idea is then to serve this dashboard in one of our FastAPI endpoints.
# -------------------------------------------------------


# Let’s serve our data drift dashboard:
@app.get("/monitoring", tags=["Other"])
def monitoring():
    dashboard_location = generate_dashboard()
    return FileResponse(dashboard_location)
