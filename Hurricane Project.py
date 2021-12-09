# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def updated_damages(damages):
    damage_list = []
    conversion = {"M": 1000000, "B": 1000000000}
    for damage in damages:
        if "M" in damage:
            damage_list.append(float(damage.strip("M")) * conversion["M"])

        elif "B" in damage:
            damage_list.append(float(damage.strip("B")) * conversion["B"])

        else:
            damage_list.append(damage)
    return damage_list

damages_updated = updated_damages(damages)


# write your construct hurricane dictionary function here:
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths):
    cane_dict = {}
    for i in range(len(names)):
        cane_dict[names[i]] = {"Name": names[i],
                               "Month": months[i],
                               "Year": years[i],
                               "Max Sustained Wind": max_sustained_winds[i],
                               "Area Affected": areas_affected[i],
                               "Damage": damages_updated[i],
                               "Deaths": deaths[i]
                               }
    return cane_dict
#print(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths))



# write your construct hurricane by year dictionary function here:
current_dictionary = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)

def hurricane_by_year(current_dictionary):
    year_hurricane = {}
    for dicts in current_dictionary:
        current_year = current_dictionary[dicts]["Year"]

        if current_year not in year_hurricane:
            year_hurricane[current_year] = current_dictionary[dicts]
        else:
            year_hurricane[current_year].update(current_dictionary[dicts])
    return year_hurricane

hurricane_by_year = hurricane_by_year(current_dictionary)
#print(hurricane_by_year(current_dictionary)[1928])

# write your count affected areas function here:

def area_affected_frequency(current_dictionary):
    area_affected_count = {}
    for dicts in current_dictionary:
        for area in current_dictionary[dicts]["Area Affected"]:
            if area not in area_affected_count:
                area_affected_count[area] = 1
            else:
                area_affected_count[area] += 1
    return area_affected_count

area_affected_count = area_affected_frequency(current_dictionary)
#print(area_affected_count)


# write your find most affected area function here:

def highest_affected_area(area_affected_count):
    max_city = "Default"
    max_count = 0
    for area in area_affected_count:
        if area_affected_count[area] > max_count:
            max_city = area
            max_count = area_affected_count[area]
    return max_city, max_count

max_area, max_area_count = highest_affected_area(area_affected_count)
#print(max_area," -> ", max_area_count)

# write your greatest number of deaths function here:

def max_num_death(current_dictionary):
    hurricane_name = "Default"
    max_num = 0
    for death in current_dictionary:
        if current_dictionary[death]["Deaths"] > max_num:
            hurricane_name = current_dictionary[death]["Name"]
            max_num = current_dictionary[death]["Deaths"]
    return hurricane_name, max_num


hurricane_name, max_mortality = max_num_death(current_dictionary)
#print(hurricane_name," -> ", max_mortality)


# write your categories by mortality function here:

def categorize_mortality(current_dictionary):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    scale_sort = {0: [],
                  1: [],
                  2: [],
                  3: [],
                  4: [],
                  }

    for dicts in current_dictionary:
        deaths = current_dictionary[dicts]["Deaths"]
        if deaths == "Damages not recorded":
            scale_sort[0].append(current_dictionary[dicts])
        elif deaths >= mortality_scale[0] and deaths < mortality_scale[1]:
            scale_sort[0].append(current_dictionary[dicts])
        elif deaths >= mortality_scale[1] and deaths < mortality_scale[2]:
            scale_sort[1].append(current_dictionary[dicts])
        elif deaths >= mortality_scale[2] and deaths < mortality_scale[3]:
            scale_sort[2].append(current_dictionary[dicts])
        elif deaths >= mortality_scale[3] and deaths < mortality_scale[4]:
            scale_sort[3].append(current_dictionary[dicts])
        else:
            scale_sort[4].append(current_dictionary[dicts])

    return scale_sort


#print(categorize_mortality(current_dictionary)[0])

# write your greatest damage function here:
print(current_dictionary)
def greatest_damage(current_dictionary):
    greatest_dam = 0
    hurricane_name = "Default"
    for dicts in current_dictionary:
        if current_dictionary[dicts]["Damage"] != "Damages not recorded" and current_dictionary[dicts]["Damage"] > greatest_dam:
            greatest_dam = current_dictionary[dicts]["Damage"]
            hurricane_name = current_dictionary[dicts]["Name"]
    return greatest_dam, hurricane_name

high_damage, cane_name = greatest_damage(current_dictionary)
print("Highest Damage: ", high_damage,"\nHurricane Name: ", cane_name)


# write your catgeorize by damage function here:
def categorize_damage(current_dictionary):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    scale = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: []
    }
    for dicts in current_dictionary:
        if current_dictionary[dicts]["Damage"] == "Damages not recorded":
            scale[0].append(current_dictionary[dicts])
        elif current_dictionary[dicts]["Damage"] >= damage_scale[0] and current_dictionary[dicts]["Damage"] <= damage_scale[1]:
            scale[0].append(current_dictionary[dicts])
        elif current_dictionary[dicts]["Damage"] >= damage_scale[1] and current_dictionary[dicts]["Damage"] <= damage_scale[2]:
            scale[1].append(current_dictionary[dicts])
        elif current_dictionary[dicts]["Damage"] >= damage_scale[2] and current_dictionary[dicts]["Damage"] <= damage_scale[3]:
            scale[2].append(current_dictionary[dicts])
        elif current_dictionary[dicts]["Damage"] >= damage_scale[3] and current_dictionary[dicts]["Damage"] <= damage_scale[4]:
            scale[3].append(current_dictionary[dicts])
        else:
            scale[4].append(current_dictionary[dicts])
    return scale

print(categorize_damage(current_dictionary)[4])