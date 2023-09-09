import json
from django.contrib.postgres.models import JSONField

import dbmodels

JSON_FOLDER_PATH = "../raw_data"

GAMES_JSON_FILE_PATH = JSON_FOLDER_PATH + "/games.json";
PLAYERS_JSON_FILE_PATH = JSON_FOLDER_PATH + "/players.json";
TEAMS_JSON_FILE_PATH = JSON_FOLDER_PATH + "/teams.json";

# Load the JSON data
with open(GAMES_JSON_FILE_PATH) as json_file:
    json_data = json.load(json_file)

# Loop through the JSON data
for record in json_data:
    # Create a Product object
    game = dbmodels.Games()

    # Set the game attributes
    game.id = record["id"]
    game.date = record["date"]
    game.homeTeam = record["homeTeam"]
    game.awayTeam = record["awayTeam"]

    # Save the Product object
    game.save()

# Load the JSON data
with open(PLAYERS_JSON_FILE_PATH) as json_file:
    json_data = json.load(json_file)

# Loop through the JSON data
for record in json_data:
    # Create a Product object
    product = dbmodels.Players()

    # Set the product attributes
    product.product_id = record["product_id"]
    product.product_name = record["product_name"]
    product.product_price = record["product_price"]

    # Save the Product object
    product.save()

# Load the JSON data
with open(TEAMS_JSON_FILE_PATH) as json_file:
    json_data = json.load(json_file)

# Loop through the JSON data
for record in json_data:
    # Create a Product object
    product = dbmodels.Teams()

    # Set the product attributes
    product.product_id = record["product_id"]
    product.product_name = record["product_name"]
    product.product_price = record["product_price"]

    # Save the Product object
    product.save()
