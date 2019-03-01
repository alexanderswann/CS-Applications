def nbaPlayerId():
    import os, ssl, json
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context
    import urllib.request
    playerFirst = input('enter a current nba players first name ' )
    playerLast = input('enter a current nba players last name ' )
    url = 'http://www.nba.com/players/'+ playerFirst+ '/' + playerLast
    x = urllib.request.urlopen(url)
    xx =  str(x.read())
    playerid = ''
    for i in range(len(xx)):
        if xx[i] == 'd' and xx[i+1] == 'a' and xx[i+2] == 't' and xx[i+3] == 'a' and xx[i+4] == '-' and xx[i+5] == 'p':
            while xx[i+15] != '"':
                playerid += xx[i+15]
                i +=1
            dataurl = 'https://data.nba.net/prod/v1/2018/players/' + playerid + '_profile.json'
            datax = urllib.request.urlopen(dataurl)
            dataxx =  str(datax.read())

            jsondata = dataxx[2:len(dataxx)-1:]

            data = json.loads(jsondata)#jsondata['league']['standard']['stats']['careerSummary']['blocks']

            careerpoints = data['league']['standard']['stats']['careerSummary']['points']
            careertpp = data['league']['standard']['stats']['careerSummary']['tpp']
            careerfgp = data['league']['standard']['stats']['careerSummary']['fgp']
            careerppg = data['league']['standard']['stats']['careerSummary']['ppg']
            careerrpg = data['league']['standard']['stats']['careerSummary']['rpg']
            careerapg = data['league']['standard']['stats']['careerSummary']['apg']
            careermpg = data['league']['standard']['stats']['careerSummary']['mpg']
            careerbpg = data['league']['standard']['stats']['careerSummary']['bpg']
            careergp = data['league']['standard']['stats']['careerSummary']['gamesPlayed']

            statfile = open(playerFirst+playerLast+'stats.txt', 'w')
            #statfile.write(playerFirst+ " "+playerLast+" has scored " + points + ' points in his career')
            statfile.write(playerFirst+ " "+playerLast+' career stats:' +'\n' + "Total Points "+ careerpoints + '\n' + "Three Point % " + careertpp+ '\n' + "Field Goal % " + careerfgp+ '\n' + "Points Per Game " + careerppg + '\n' + "Rebounds Per Game " + careerrpg + '\n' + "Assists Per Game " + careerapg  + '\n' + "Minutes Per Game " + careermpg+ '\n' + "Blocks Per Game " + careerbpg + '\n' + "Total Games Played " + careergp    )
            # statfile.write(jsondata)
            statfile.close()
            return data['league']['standard']['stats']['careerSummary']
print(nbaPlayerId())
