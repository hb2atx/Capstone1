from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()

bcrypt = Bcrypt()



def connect_db(app):
        ######## CONNECT TO DATABASE ###########
        db.app = app
        db.init_app(app)

        


########## MODELS ###########

class User(db.Model):
        
        __tablename__ = "users"

        id = db.Column(db.Integer   , primary_key=True)
        username = db.Column(db.String)
        password = db.Column(db.String)

class DefensiveSkillPlayers(db.Model):
        
        __tablename__ = "defense"

        id = db.Column(db.Integer, primary_key=True)
        position = db.Column(db.String)
        activated = db.Column(db.Integer)
        season = db.Column(db.Integer)
        name = db.Column(db.String, nullable=False)
        position_category = db.Column(db.String)
        player_id = db.Column(db.Integer)
        team = db.Column(db.String)
        solo_tackles = db.Column(db.Integer)
        tackles = db.Column(db.Integer)
        assisted_tackles = db.Column(db.Integer)
        fumbles_forced = db.Column(db.Integer)
        fumbles_recovered = db.Column(db.Integer)
        interceptions = db.Column(db.Integer)
        played = db.Column(db.Integer)


class OffensiveSkillPlayers(db.Model):

        __tablename__ = "offensive_players"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, nullable=False)
        season = db.Column(db.Integer)
        activated = db.Column(db.Integer)
        position = db.Column(db.String)
        position_category = db.Column(db.String)
        player_id = db.Column(db.Integer)
        team = db.Column(db.String)
        fumbles = db.Column(db.Integer)
        receptions = db.Column(db.Integer)
        receiving_yards_per_reception = db.Column(db.Integer)
        receiving_targets = db.Column(db.Integer)
        receiving_touchdowns = db.Column(db.Integer)
        receiving_yards = db.Column(db.Integer)
        rushing_attempts = db.Column(db.Integer)
        rushing_touchdowns = db.Column(db.Integer)
        rushing_yards = db.Column(db.Integer)
        rushing_yards_per_attempt = db.Column(db.Integer)
        rushing_long = db.Column(db.Integer)
        played = db.Column(db.Integer)

class OffensiveLine(db.Model):
        
        __tablename__ = "offensive_line"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String)
        activated = db.Column(db.Integer)
        season = db.Column(db.Integer)
        position_category = db.Column(db.String)
        player_id = db.Column(db.Integer)
        team = db.Column(db.String)
        position = db.Column(db.String)
        offensive_team_snaps = db.Column(db.Integer)
        offensive_snaps_played = db.Column(db.Integer)
        started = db.Column(db.Integer)
        played = db.Column(db.Integer)

      
class Qb(db.Model):
        
        __tablename__ = "qbs"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String)
        # season = db.Column(db.Integer)
        activated = db.Column(db.Integer)
        position_category = db.Column(db.String)
        player_id = db.Column(db.Integer)
        position = db.Column(db.String)
        fumbles = db.Column(db.Integer)
        played = db.Column(db.Integer)
        team = db.Column(db.String)
        passing_completion_percentage = db.Column(db.Integer)
        passing_completions = db.Column(db.Integer)
        passing_receptions = db.column(db.Integer)
        passing_rating = db.Column(db.Integer)
        passing_touchdowns = db.Column(db.Integer)
        passing_yards = db.Column(db.Integer)
        rushing_attempts = db.Column(db.Integer)
        rushing_yards = db.Column(db.Integer)
        rushing_touchdowns = db.Column(db.Integer)

     


class Punter(db.Model):
        
        __tablename__ = "punters"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String)
        season = db.Column(db.Integer)
        activated = db.Column(db.Integer)
        position_category = db.Column(db.String)
        player_id = db.Column(db.Integer)
        position = db.Column(db.String)
        team = db.Column(db.String)
        punt_average = db.Column(db.Integer)
        punt_inside_20 = db.Column(db.Integer)
        punt_net_yards = db.Column(db.Integer)
        punt_long = db.Column(db.Integer)
        punts = db.Column(db.Integer)

      

class Kicker(db.Model):
        
        __tablename__ = "kickers"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String)
        season = db.Column(db.Integer)
        activated = db.Column(db.Integer)
        position_category = db.Column(db.String)
        player_id = db.Column(db.Integer)
        team = db.Column(db.String)
        position = db.Column(db.String)
        field_goals_attempted = db.Column(db.Integer)
        field_goal_percentage = db.Column(db.Integer)
        field_goals_made = db.Column(db.Integer)
        field_goals_made_0_to_19 = db.Column(db.Integer)
        field_goals_made_20_to_29 = db.Column(db.Integer)
        field_goals_made_30_to_39 = db.Column(db.Integer)
        field_goals_made_40_to_49 = db.Column(db.Integer)
        field_goals_made_50_plus = db.Column(db.Integer)
        field_goals_longest_made = db.Column(db.Integer)


class Team(db.Model):
        
        __tablename__ = "teams"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String)
        team_id = db.Column(db.Integer)




     
        






                
              












 
          








   