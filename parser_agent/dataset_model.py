from enum import Enum
from typing import List, Optional, Tuple

from pydantic import BaseModel, Field


class PageType(str, Enum):
    """Type of page"""

    country = "country"
    city = "city"
    attraction = "attraction"
    landmark = "landmark"
    other = "other"
    unknown = "unknown"

    @classmethod
    def _missing_(cls, value):
        return cls.unknown


class Page(BaseModel):
    page_type: PageType = Field(
        description=f"""Page type, can be one of {", ".join([e for e in PageType])}"""
    )


class ClimateType(str, Enum):
    """Type of climate at the location"""

    tropical = "tropical"
    desert = "desert"
    temperate = "temperate"
    continental = "continental"
    polar = "polar"
    unknown = "unknown"

    @classmethod
    def _missing_(cls, value):
        return cls.unknown


class ActivityType(str, Enum):
    """Type of activities and attractions available at the location"""

    # Social and Nightlife
    partying = "partying"
    clubbing = "clubbing"
    bars_and_pubs = "bars and pubs"
    live_music = "live music"
    comedy_clubs = "comedy clubs"

    # Nature and Outdoors
    nature = "nature"
    hiking = "hiking"
    camping = "camping"
    birdwatching = "birdwatching"
    stargazing = "stargazing"
    outdoor_activities = "outdoor activities"
    scenic_drives = "scenic drives"
    wildlife_viewing = "wildlife viewing"

    # Water and Aquatic
    aquatic_activities = "aquatic activities"
    snorkeling = "snorkeling"
    scuba_diving = "scuba diving"
    surfing = "surfing"
    kayaking = "kayaking"
    paddleboarding = "paddleboarding"
    boat_tours = "boat tours"
    fishing = "fishing"

    # Family and Children
    children_activities = "children activities"
    amusement_parks = "amusement parks"
    water_parks = "water parks"
    zoos_and_aquariums = "zoos and aquariums"
    museums_for_kids = "museums for kids"
    playgrounds = "playgrounds"

    # Sports and Fitness
    sports = "sports"
    running = "running"
    cycling = "cycling"
    swimming = "swimming"
    golfing = "golfing"
    skiing = "skiing"
    snowboarding = "snowboarding"
    team_sports = "team sports"

    # Wellness and Relaxation
    wellness = "wellness"
    spas = "spas"
    yoga = "yoga"
    meditation = "meditation"
    saunas_and_hot_tubs = "saunas and hot tubs"
    massage = "massage"

    # Culture and History
    cultural = "cultural"
    historical = "historical"
    museums = "museums"
    art_galleries = "art galleries"
    landmarks = "landmarks"
    historical_sites = "historical sites"
    cultural_events = "cultural events"

    # Food and Drink
    food_and_wine = "food and wine"
    wine_tasting = "wine tasting"
    brewery_tours = "brewery tours"
    coffee_shops = "coffee shops"
    restaurants = "restaurants"
    cooking_classes = "cooking classes"
    food_tours = "food tours"

    # Shopping and Retail
    shopping = "shopping"
    malls = "malls"
    markets = "markets"
    boutiques = "boutiques"
    souvenir_shops = "souvenir shops"
    antique_shops = "antique shops"

    # Entertainment and Performance
    entertainment = "entertainment"
    movies = "movies"
    theater = "theater"
    music_venues = "music venues"
    comedy_shows = "comedy shows"
    magic_shows = "magic shows"

    # Education and Learning
    educational = "educational"
    workshops = "workshops"
    conferences = "conferences"
    seminars = "seminars"
    classes = "classes"
    lectures = "lectures"

    # Spirituality and Faith
    spiritual = "spiritual"
    churches = "churches"
    temples = "temples"
    mosques = "mosques"
    synagogues = "synagogues"
    meditation_retreats = "meditation retreats"

    # Games and Recreation
    games = "games"
    escape_rooms = "escape rooms"
    game_centers = "game centers"
    bowling = "bowling"
    laser_tag = "laser tag"
    mini_golf = "mini golf"

    # Adventure and Thrills
    adventure = "adventure"
    skydiving = "skydiving"
    bungee_jumping = "bungee jumping"
    rock_climbing = "rock climbing"
    zip_lining = "zip lining"
    white_water_rafting = "white water rafting"
    hunting = "hunting"

    unknown = "unknown"

    @classmethod
    def _missing_(cls, value):
        return cls.unknown


class Attraction(BaseModel):
    """Model for an attraction"""

    name: str = Field(..., description="Name of the attraction")
    description: str = Field(..., description="Description of the attraction")
    city: str = Field(
        ..., description="City where the attraction is located or is closest to"
    )
    country: str = Field(
        ..., description="Country where the attraction is or is closest to"
    )
    activity_types: List[ActivityType] = Field(
        ...,
        description="List of activity types and attractions available at the attraction",
    )
    tags: List[str] = Field(
        ...,
        description="List of tags describing the attraction (e.g. accessible, sustainable, sunny, cheap, pricey)",
        min_length=1,
    )


class City(BaseModel):
    """Model for a tourist location"""

    name: str = Field(..., description="Name of the city")
    description: str = Field(
        ...,
        description="Few sentences description of the city, can be long if there is enough "
        "relevant information. Includes what the city is famous for and why people might visit it.",
    )

    country: str = Field(..., description="Country")
    continent: Optional[str] = Field(
        None, description="Continent if applicable, otherwise leave empty"
    )

    location_lat_long: Optional[list[float]] = Field(
        [],
        description="Geographic coordinates [latitude, longitude] of the location, [] if unknown",
    )
    climate_type: ClimateType = Field(..., description="Type of climate at the city")

    class Config:
        use_enum_values = True
        extra = "forbid"


class Cities(BaseModel):
    """Model for a tourist locations"""

    cities: List[City] = Field(..., description="List of Locations")


class Attractions(BaseModel):
    """Model for a tourist locations"""

    attractions: List[Attraction] = Field(..., description="List of Attractions")


city_example = City(
    name="ABC",
    country="DEF",
    continent="",
    location_lat_long=[-1, 1],
    climate_type=ClimateType.tropical,
    description="GHI",
)

attraction_example = Attraction(
    name="Teamlabs Borderless",
    description="Light Museum",
    city="Tokyo",
    country="Japan",
    activity_types=[ActivityType.museums, ActivityType.museums_for_kids],
    tags=["Art"],
)

page_example = Page(page_type=PageType.other)

if __name__ == "__main__":
    print(city_example.model_dump_json())
    print(city_example.model_json_schema())

    print(attraction_example.model_dump_json())
    print(attraction_example.model_json_schema())
