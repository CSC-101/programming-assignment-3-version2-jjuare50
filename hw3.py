import data
import build_data


# Task 1
def population_total(counties: list[data.CountyDemographics]) -> int:
    total_population = 0
    for county in counties:
        total_population += county.population["2014 Population"]
    return total_population

# Task 2

def filter_by_state(counties: list[data.CountyDemographics], state: str) -> list[data.CountyDemographics]:

    filtered_counties = []
    for county in counties:
        if county.state == state:
            filtered_counties.append(county)
    return filtered_counties

# Task 3

def population_by_education(counties: list[data.CountyDemographics], education: str) -> float:
    sub_population = 0.0
    for county in counties:
        if education in county.education.keys():
            eduction_population = county.education[education]
            total_population = county.population["2014 Population"]
            sub_population += (eduction_population / 100.0) * total_population
            return sub_population
        else:
            return 0.0

def population_by_ethnicity(counties: list[data.CountyDemographics], ethnicity: str) -> float:
    sub_population = 0.0
    for county in counties:
        if ethnicity in county.ethnicities.keys():
            ethnicity_population = county.ethnicities[ethnicity]
            total_population = county.population["2014 Population"]
            sub_population += (ethnicity_population / 100.0) * total_population
            return sub_population
        else:
            return 0.0

def population_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    total_below_poverty = 0.0
    for county in counties:
        county_poverty = county.income["Persons Below Poverty Level"]
        county_population = county.population["2014 Population"]
        total_below_poverty += (county_poverty / 100.0) * county_population
    return total_below_poverty

# Task 4
def percent_by_education(counties: list[data.CountyDemographics], education_type: str) -> float:
    total_population = 0.0
    sub_population = 0.0
    for county in counties:
        if education_type in county.education.keys():
            sub_population += (county.education[education_type] / 100) * county.population["2014 Population"]
        else:
            return 0.0
        total_population += county.population["2014 Population"]
    return (sub_population / total_population) * 100


def percent_by_ethnicity(counties: list[data.CountyDemographics], ethnicity: str) -> float:
    total_population = 0.0
    sub_population = 0.0
    for county in counties:
        if ethnicity in county.ethnicities.keys():
            sub_population += (county.ethnicities[ethnicity] / 100) * county.population["2014 Population"]
        else:
            return 0.0
        total_population += county.population["2014 Population"]
    return (sub_population / total_population) * 100

def percent_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    total_population = 0.0
    sub_population = 0.0
    for county in counties:
        sub_population += (county.income["Persons Below Poverty Level"] / 100) * county.population["2014 Population"]
        total_population += county.population["2014 Population"]
    return (sub_population / total_population) * 100

# Task 5

def education_greater_than(counties: list[data.CountyDemographics], education: str, threshold: float) -> list[data.CountyDemographics]:
    new_counties = []
    for county in counties:
        if county.education[education] > threshold:
            new_counties.append(county)
    return new_counties

def education_less_than(counties: list[data.CountyDemographics], education: str, threshold: float) -> list[data.CountyDemographics]:
    new_counties = []
    for county in counties:
        if county.education[education] < threshold:
            new_counties.append(county)
    return new_counties

def ethnicity_less_than(counties: list[data.CountyDemographics], ethnicity: str, threshold: float) -> list[data.CountyDemographics]:
    new_counties = []
    for county in counties:
        if county.ethnicities[ethnicity] < threshold:
            new_counties.append(county)
    return new_counties


def ethnicity_greater_than(counties: list[data.CountyDemographics], ethnicity: str, threshold: float) -> list[data.CountyDemographics]:
    new_counties = []
    for county in counties:
        if county.ethnicities[ethnicity] > threshold:
            new_counties.append(county)
    return new_counties

def below_poverty_level_greater_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    new_counties = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] > threshold:
            new_counties.append(county)
    return new_counties

def below_poverty_level_less_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    new_counties = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] < threshold:
            new_counties.append(county)
    return new_counties
















