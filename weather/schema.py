import requests
import graphene

class WeatherType(graphene.ObjectType):
    temperature = graphene.Float()
    windspeed = graphene.Float()

class Query(graphene.ObjectType):
    get_weather = graphene.Field(WeatherType, latitude=graphene.Float(), longitude=graphene.Float())

    def resolve_get_weather(self, info, latitude=52.2298, longitude=21.0122):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url, timeout=5).json()
        weather_data = response.get("current_weather", {})
        return WeatherType(
            temperature=weather_data.get("temperature"),
            windspeed=weather_data.get("windspeed"),
        )

schema = graphene.Schema(query=Query)
