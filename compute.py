import requests
import csv


def calcES(playerArating, playerBrating):
    return 1 / (1 + 10 ** ((playerBrating - playerArating)/400))

def get_scores():


    colors = requests.get("https://docs.google.com/spreadsheets/d/1qV4nsOQXwV_Y6iyPH66sz4SuetZZkRM3Qsljs6SadbQ/gviz/tq?tqx=out:csv&sheet=colors").text
    color_sheet = csv.reader(colors.split("\n"))
    colors = {}
    for row in color_sheet:
        colors[row[0]] = row[1]

    games_webpage = requests.get(
        'https://docs.google.com/spreadsheets/d/1qV4nsOQXwV_Y6iyPH66sz4SuetZZkRM3Qsljs6SadbQ/gviz/tq?tqx=out:csv').text

    game_sheet = csv.reader(games_webpage.split("\n"))
    next(game_sheet)
    next(game_sheet)
    games = []
    players = {}
    for row in game_sheet:
        games.append((row[0], row[1]))

    for game in games:
        for player in game:
            if player not in players:
                players[player] = 1600
        playerA = game[0]
        playerB = game[1]
        ratingA = players[playerA]
        ratingB = players[playerB]
        AES = calcES(ratingB, ratingA)
        players[playerA] = ratingA + 32*AES
        players[playerB] = ratingB - 32*AES

    players = sorted(players.items(), key=lambda x: x[1], reverse=True)

    return [player + (colors[player[0]],) for player in players]

