# 3rd-pre-deliverableVictor

### views.py
As a first step I have created in the views.py a function where we set a greeting message to the Atletico de Madrid Fans (Hi Atleti Fans!)

### urls.py
I have created the routing between the URLs project my_football_team and the applicaiton atletico_de_madrid, with that working the requests coming from the user will work properly.

### models.py
In the models.py we set the Classes to insert information in the database sqlite, please use the below script from django python shell in order to insert data into the database.

-py manage.py shell<br>
-from atletico_de_madrid.models import TeamCategory, Players<br>
-team = TeamCategory(team_name="Atletico A", location="Spain, Madrid")<br>
-team.save()<br>

### Code for updating team type

team.team_name = "Atletico B"<br>
team.save()<br>

### Code for adding players.

Players(name="Marcos Llorente", age="27", team=team).save()<br><br>
Players(name="Antonie Griezman", age="31", team=team).save()<br>
Then go to SQLite database and see the changes done.<br>
