import requests
from pprint import pprint
from app import app
from models import db, Qb, OffensiveSkillPlayers, Kicker, Punter, DefensiveSkillPlayers, OffensiveLine



TEAMS = {"ARI","ATL","BAL","BUFF","CAR","CHI","CIN","CLE","DAL","DEN","DET","GB","HOU","IND","JAX","KC","LV","LAC","LAR","MIA","MIN","NE","NO","NYG","NYJ","PHI","PIT","SF","SEA","TB","TEN","WAS"}
OFFENSIVE_SKILL_PLAYERS = {"QB", "RB", "WR", "TE", "K", "P", "FB", "OL", "C", "RT", "RG", "LG", "LT", "K", "P"}
DEFENSIVE_SKILL_PLAYERS = {"DL", "DE", "LB", "CB", "SS", "FS"}

for team in TEAMS:
    team_data = requests.get(f"https://api.sportsdata.io/v3/nfl/stats/json/PlayerSeasonStatsByTeam/2022/{team}?key=10945f321a31476a9e6038dd680f7655")
    response = team_data.json()
    for key in response:
      if key["PositionCategory"] == "OFF" and key["Position"] in OFFENSIVE_SKILL_PLAYERS:
         name = key["Name"]
         position = key["Position"]
         played = key["Played"]
         season = key["Season"]
         player_id = key["PlayerID"]
         position_category = key["PositionCategory"]
         activated = key["Activated"]
         team = key["Team"]
         rushing_yards = key["RushingYards"]
         rushing_attempts = key["RushingAttempts"]
         rushing_touchdowns = key["RushingTouchdowns"]
         rushing_yards_per_attempt = key["RushingYardsPerAttempt"]
         rushing_long = key["RushingLong"]
         fumbles = key["Fumbles"]
         passing_yards = key["PassingYards"]
         passing_touchdowns = key["PassingTouchdowns"]
         passing_completion_percentage = key["PassingCompletionPercentage"]
         passing_completions = key["PassingCompletions"]
         passing_rating = key["PassingRating"]
         receiving_targets = key["ReceivingTargets"]
         receptions = key["Receptions"]
         receiving_yards = key["ReceivingYards"]
         receiving_yards_per_reception = key["ReceivingYardsPerReception"]
         receiving_touchdowns = key["ReceivingTouchdowns"]
         punt_inside_20 = key["PuntInside20"]
         punt_net_average = key["PuntNetAverage"]
         punt_long = key["PuntLong"]
         punts = key["Punts"]
         punt_yards = key["PuntYards"]
         punt_average = key["PuntAverage"]

         

         if position == "QB":
            qb = Qb(name=name, position=position, rushing_yards=rushing_yards,rushing_attempts=rushing_attempts,rushing_touchdowns=rushing_touchdowns,passing_yards=passing_yards, passing_touchdowns=passing_touchdowns,passing_completion_percentage=passing_completion_percentage,
                    passing_completions=passing_completions,passing_rating=passing_rating, played=played, team=team, activated=activated,
                    player_id=player_id,position_category=position_category, fumbles=fumbles)
            
            db.session.add(qb)
            db.session.commit()

            if position == "RB":
               rb = OffensiveSkillPlayers(name=name, position=position, rushing_yards=rushing_yards,rushing_attempts=rushing_attempts,
                       rushing_touchdowns=rushing_touchdowns, played=played, rushing_yards_per_attempt=rushing_yards_per_attempt,
                       rushing_long=rushing_long, fumbles=fumbles, season=season, player_id=player_id,
                       position_category=position_category, activated=activated, team=team, receiving_yards=receiving_yards)
               
               db.session.add(rb)
               db.session.commit()

               if position == "WR":
                  wr = OffensiveSkillPlayers(name=name, position=position, played=played, team=team, activated=activated,
                    player_id=player_id, season=season, position_category=position_category, fumbles=fumbles,
                    receiving_targets=receiving_targets, receptions=receptions, receiving_yards_per_reception=receiving_yards_per_reception,
                    receiving_touchdowns=receiving_touchdowns)
                  
                  db.session.add(wr)
                  db.session.commit()

                  if position == "TE":
                     te = OffensiveSkillPlayers(name=name, position=position, played=played, team=team, activated=activated,
                    player_id=player_id, season=season, position_category=position_category, fumbles=fumbles,
                    receiving_targets=receiving_targets, receptions=receptions, receiving_yards_per_reception=receiving_yards_per_reception,
                    receiving_touchdowns=receiving_touchdowns)
                     
                  db.session.add(te)
                  db.session.commit()

                  if position == "FB":
                     fb = OffensiveSkillPlayers(name=name, position=position, rushing_yards=rushing_yards,rushing_attempts=rushing_attempts,
                       rushing_touchdowns=rushing_touchdowns, played=played, rushing_yards_per_attempt=rushing_yards_per_attempt,
                       rushing_long=rushing_long, fumbles=fumbles, season=season, player_id=player_id,
                       position_category=position_category, activated=activated, team=team, receiving_yards=receiving_yards)
                  db.session.add(fb)
                  db.session.commit()

            elif key["PositionCategory"] == "ST" and key["Position"] == OFFENSIVE_SKILL_PLAYERS:
                   name = key["Name"]
                   position = key["Position"]
                   played = key["Played"]
                   season = key["Season"]
                   player_id = key["PlayerID"]
                   position_category = key["PositionCategory"]
                   activated = key["Activated"]
                   team = key["Team"]
                   field_goals_attempted = key["FieldGoalsAttempted"]
                   field_goals_made = key["FieldGoalsMade"]
                   field_goals_longest_made = key["FieldGoalsLongestMade"]
                   extra_points_made = key["ExtraPointsMade"]
                   field_goals_made_0_to_19 = key["FieldGoalsMade0to19"]
                   field_goals_made_20_to_29 = key["FieldGoalsMade20to29"]
                   field_goals_made_30_to_39 = key["FieldGoalsMade30to39"]
                   field_goals_made_40_to_49 = key["FieldGoalsMade40to49"]
                   field_goals_made_50_plus = key["FieldGoalsMade50Plus"]

                     
                   if position == "K":
                        k = Kicker(name=name, position=position, position_category=position_category, activated=activated, team=team,
                              season=season, player_id=player_id, field_goals_attempted=field_goals_attempted,
                              field_goals_made=field_goals_made, field_goals_longest_made=field_goals_longest_made,
                              extra_points_made=extra_points_made,  field_goals_made_0_to_19= field_goals_made_0_to_19,
                              field_goals_made_20_to_29=field_goals_made_20_to_29, field_goals_made_30_to_39=field_goals_made_30_to_39,
                              field_goals_made_50_plus=field_goals_made_50_plus)
                        
                   db.session.add(k)
                   db.session.commit()
            
            elif key["PositionCategory"] == "ST" and key["Position"] == OFFENSIVE_SKILL_PLAYERS:
             name = key["Name"]
             position = key["Position"]
             played = key["Played"]
             season = key["Season"]
             player_id = key["PlayerID"]
             position_category = key["PositionCategory"]
             activated = key["Activated"]
             team = key["Team"]
             punt_inside_20 = key["PuntInside20"]
             punt_net_average = key["PuntNetAverage"]
             punt_long = key["PuntLong"]
             punts = key["Punts"]
             punt_yards = key["PuntYards"]
             punt_average = key["PuntAverage"]
            

            if position == "P":
                     p = Punter(name=name, position=position, position_category=position_category, activated=activated, team=team,
                              season=season, player_id=player_id, punt_inside_20=punt_inside_20, punt_net_average=punt_net_average,
                              punt_long=punt_long, punts=punts, punt_yards=punt_yards, punt_average=punt_average, )
                     
                     db.session.add(p)
                     db.session.commit()

            elif key["PositionCategory"] == "OFF" and key["Position"] in OFFENSIVE_SKILL_PLAYERS:
                  name = key["Name"]
                  position = key["Position"]
                  played = key["Played"]
                  season = key["Season"]
                  player_id = key["PlayerID"]
                  position_category = key["PositionCategory"]
                  activated = key["Activated"]
                  team = key["Team"]
                  offensive_snaps_played = key["OffensiveSnapsPlayed"]

                  if position == "OL":
                     ol = OffensiveLine(name=name, position=position, position_category=position_category, activated=activated, 
                                        team=team, season=season, player_id=player_id, played=played, offensive_snaps_played=offensive_snaps_played)
                     
                     db.session.add(ol)
                     db.session.commit()
                     
                  if position == "LT":
                     lt = OffensiveLine(name=name, position=position, position_category=position_category, activated=activated, 
                                        team=team, season=season, player_id=player_id, played=played, offensive_snaps_played=offensive_snaps_played)
                     
                     db.session.add(lt)
                     db.session.commit()
                     
                  if position == "RT":
                     rt = OffensiveLine(name=name, position=position, position_category=position_category, activated=activated, 
                                        team=team, season=season, player_id=player_id, played=played, offensive_snaps_played=offensive_snaps_played)
                     
                     db.session.add(rt)
                     db.session.commit()
                     
                  if position == "RG":
                     rg = OffensiveLine(name=name, position=position, position_category=position_category, activated=activated, 
                                        team=team, season=season, player_id=player_id, played=played, offensive_snaps_played=offensive_snaps_played)
                     
                     db.session.add(rg)
                     db.session.commit()
                     
                  if position == "LG":
                     lg = OffensiveLine(name=name, position=position, position_category=position_category, activated=activated, 
                                        team=team, season=season, player_id=player_id, played=played, offensive_snaps_played=offensive_snaps_played)
                     
                     db.session.add(lg)
                     db.session.commit()
                     
                  if position == "C":
                     c = OffensiveLine(name=name, position=position, position_category=position_category, activated=activated, 
                                        team=team, season=season, player_id=player_id, played=played, offensive_snaps_played=offensive_snaps_played)
                     
                     db.session.add(c)
                     db.session.commit()

               
                     

            elif key["PositionCategory"] == "DEF" and key["Position"] in DEFENSIVE_SKILL_PLAYERS:
                     name = key["Name"]
                     position = key["Position"]
                     played = key["Played"]
                     season = key["Season"]
                     player_id = key["PlayerID"]
                     position_category = key["PositionCategory"]
                     activated = key["Activated"]
                     team = key["Team"]
                     sacks = key["Sacks"]
                     tackles_for_loss = key["TacklesForLoss"]
                     solo_tackles = key["SoloTackles"]
                     assisted_tackles = key["AssistedTackles"]
                     sack_yards = key["SackYards"]
                     passes_defended = key["PassesDefended"]
                     fumbles_forced = key["FumblesForced"]
                     fumbles_recovered = key["FumblesRecovered"]
                     interceptions = key["Interceptions"]
                     interception_return_touchdowns = key["InterceptionReturnTouchdowns"]
                     defensive_touchdowns = key["DefensiveTouchdowns"]
                     safeties = key["Safeties"]

                     if position == "DL":
                        dl = DefensiveSkillPlayers(name=name, position=position, position_category=position_category, activated=activated, team=team,
                                                   season=season, player_id=player_id, sacks=sacks, tackles_for_loss=tackles_for_loss,
                                                   solo_tackles=solo_tackles, assisted_tackles=assisted_tackles, sack_yards=sack_yards, passes_defended=passes_defended,
                                                   fumbles_forced=fumbles_forced, fumbles_recovered=fumbles_recovered, interceptions=interceptions,
                                                   interception_return_touchdowns=interception_return_touchdowns, defensive_touchdowns=defensive_touchdowns,
                                                   safeties=safeties)
                        
                        db.session.add(dl)
                        db.session.commit()

                     if position == "DE":
                      de = DefensiveSkillPlayers(name=name, position=position, position_category=position_category, activated=activated, team=team,
                                                   season=season, player_id=player_id, sacks=sacks, tackles_for_loss=tackles_for_loss,
                                                   solo_tackles=solo_tackles, assisted_tackles=assisted_tackles, sack_yards=sack_yards, passes_defended=passes_defended,
                                                   fumbles_forced=fumbles_forced, fumbles_recovered=fumbles_recovered, interceptions=interceptions,
                                                   interception_return_touchdowns=interception_return_touchdowns, defensive_touchdowns=defensive_touchdowns,
                                                   safeties=safeties)
                      db.session.add(de)
                      db.session.commit()
                      
                      if position == "LB":
                         lb = DefensiveSkillPlayers(name=name, position=position, position_category=position_category, activated=activated, team=team,
                                                   season=season, player_id=player_id, sacks=sacks, tackles_for_loss=tackles_for_loss,
                                                   solo_tackles=solo_tackles, assisted_tackles=assisted_tackles, sack_yards=sack_yards, passes_defended=passes_defended,
                                                   fumbles_forced=fumbles_forced, fumbles_recovered=fumbles_recovered, interceptions=interceptions,
                                                   interception_return_touchdowns=interception_return_touchdowns, defensive_touchdowns=defensive_touchdowns,
                                                   safeties=safeties)
                         
                         db.session.add(lb)
                         db.session.commit()
                         
                     if position == "CB":
                        cb = DefensiveSkillPlayers(name=name, position=position, position_category=position_category, activated=activated, team=team,
                                                   season=season, player_id=player_id, sacks=sacks, tackles_for_loss=tackles_for_loss,
                                                   solo_tackles=solo_tackles, assisted_tackles=assisted_tackles, sack_yards=sack_yards, passes_defended=passes_defended,
                                                   fumbles_forced=fumbles_forced, fumbles_recovered=fumbles_recovered, interceptions=interceptions,
                                                   interception_return_touchdowns=interception_return_touchdowns, defensive_touchdowns=defensive_touchdowns,
                                                   safeties=safeties)
                        
                        db.session.add(cb)
                        db.session.commit()
                        
                     if position == "SS":
                        ss = DefensiveSkillPlayers(name=name, position=position, position_category=position_category, activated=activated, team=team,
                                                   season=season, player_id=player_id, sacks=sacks, tackles_for_loss=tackles_for_loss,
                                                   solo_tackles=solo_tackles, assisted_tackles=assisted_tackles, sack_yards=sack_yards, passes_defended=passes_defended,
                                                   fumbles_forced=fumbles_forced, fumbles_recovered=fumbles_recovered, interceptions=interceptions,
                                                   interception_return_touchdowns=interception_return_touchdowns, defensive_touchdowns=defensive_touchdowns,
                                                   safeties=safeties)
                        
                        db.session.add(ss)
                        db.session.commit()
                        
                     if position == "FS":
                        fs = DefensiveSkillPlayers(name=name, position=position, position_category=position_category, activated=activated, team=team,
                                                   season=season, player_id=player_id, sacks=sacks, tackles_for_loss=tackles_for_loss,
                                                   solo_tackles=solo_tackles, assisted_tackles=assisted_tackles, sack_yards=sack_yards, passes_defended=passes_defended,
                                                   fumbles_forced=fumbles_forced, fumbles_recovered=fumbles_recovered, interceptions=interceptions,
                                                   interception_return_touchdowns=interception_return_touchdowns, defensive_touchdowns=defensive_touchdowns,
                                                   safeties=safeties)
                        
                        db.session.add(fs)
                        db.session.commit()

                    









                           
                              
                              
                        
                        
                     


            




     




        #  print(name, position, rushing_yards, rushing_attempts, rushing_touchdowns, passing_yards, passing_touchdowns, passing_completion_percentage, passing_completions, passing_rating)

        

