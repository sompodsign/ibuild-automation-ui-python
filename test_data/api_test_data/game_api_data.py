from application_settings.api_base_requests import BaseApi
from data_provider.test_data_provider import CustomTestDataProvider


class GameData(CustomTestDataProvider):
    race_api = BaseApi('/game/api/race')

    def get_new_dog_data(self):
        races = self.race_api.get_request()
        match_id = races['response']['races'][-1]['_id']

        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": match_id,
        }

    def get_new_dog_data_without_name(self):
        return {
            "name": "",
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_age(self):
        return {
            "name": self.get_full_name(),
            "age": "",
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_weight(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": "",
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_fatigue(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": "",
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_injury(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": "",
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_acceleration(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": "",
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_top_speed(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": "",
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_power(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": "",
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_reaction_time(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": "",
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_main_weather(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": "",
            "sex": self.get_sex(),
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_sex(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": "",
            "matchId": self.get_random_id(),
        }

    def get_new_dog_data_without_matchId(self):
        return {
            "name": self.get_full_name(),
            "age": self.get_age(),
            "weight": self.get_weight(),
            "fatigue": self.get_random_number(),
            "injury": self.get_random_number(),
            "acceleration": self.get_random_number(),
            "topSpeed": self.get_random_number(),
            "power": self.get_random_number(),
            "reactionTime": self.get_random_number(),
            "mainWeather": self.get_random_number(),
            "sex": self.get_sex(),
            "matchId": "",
        }

    def get_payload_with_empty_match_id(self):
        return {
            "matchId": "",
            "dogs": [self.get_random_id()]
        }

    def get_payload_with_empty_dogs_id(self):
        return {
            "matchId": self.get_random_id(),
            "dogs": []
        }

    def get_new_race_data(self):
        return {
            "event": self.get_random_first_name(),
            "location": self.get_city(),
            "entranceFee": self.get_random_number(),
            "eventType": self.get_random_last_name(),
            "raceTime": self.get_random_time()
        }

    def get_new_race_data_without_event(self):
        return {
            "event": "",
            "location": self.get_city(),
            "entranceFee": self.get_random_number(),
            "eventType": self.get_random_last_name(),
            "raceTime": self.get_random_time()
        }

    def get_new_race_data_without_location(self):
        return {
            "event": self.get_random_first_name(),
            "location": "",
            "entranceFee": self.get_random_number(),
            "eventType": self.get_random_last_name(),
            "raceTime": self.get_random_time()
        }

    def get_new_race_data_without_entrance_fee(self):
        return {
            "event": self.get_random_first_name(),
            "location": self.get_city(),
            "entranceFee": "",
            "eventType": self.get_random_last_name(),
            "raceTime": self.get_random_time()
        }

    def get_new_race_data_without_event_type(self):
        return {
            "event": self.get_random_first_name(),
            "location": self.get_city(),
            "entranceFee": self.get_random_number(),
            "eventType": "",
            "raceTime": self.get_random_time()
        }

    def get_new_race_data_without_race_time(self):
        return {
            "event": self.get_random_first_name(),
            "location": self.get_city(),
            "entranceFee": self.get_random_number(),
            "eventType": self.get_random_last_name(),
            "raceTime": ""
        }

    def get_bet_amount(self):
        return self.get_random_number()
