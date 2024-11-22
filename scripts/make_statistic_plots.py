# Author: Nicole Schanche
# Created Oct 12, 2022
# Update Nov 4, 2022 - turned code into functions
# Update Sep 12, 2023 - 

 
import pandas as pd
import sqlite3
import json
import re
import numpy as np
import itertools
import plotly.graph_objects as go
import plotly.express as px
from datetime import date, datetime
from dateutil import rrule
import matplotlib.pyplot as plt
from collections import defaultdict
from collections import Counter
import urllib.request
import os,sys


def get_tpub(tpub_path="./tpub.db"):
    """
    Read in the latest database file from tpub (Note that this is static for now, but can be adjusted later when we decide how we want to get tpub data for the website.)

    Parameters
    ----------------
    tpub_path: File path to the tpub database

    Returns
    ------------
    results: all entries in the tpub database that are from the TESS mission
    """

    #Check to see if tpub.db exists here and if so remove
    if os.path.exists(tpub_path):
        os.remove(tpub_path)

    #Get the tpub file
    urllib.request.urlretrieve("https://github.com/tessgi/tpub/raw/master/data/tpub.db", filename=tpub_path)
    

    query = sqlite3.connect(tpub_path).execute("SELECT * FROM pubs")
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    results = results[results["mission"] == "tess"].reset_index(drop=True)

    os.remove(tpub_path)
    
    return results


# We will want to pull in some information on the author's affiliation (country and state (if applicable))
def get_countries(country_path="htmlcontent/statistics/data/countries_codes_and_coordinates.csv"):
    """
    Function to read in the csv file containing country names, codes, and lat/long coordinates

    Parameters
    ----------------
    country_path (optional): File path to the csv file

    Returns
    ------------
    countries: Pandas dataframe with country information
    """

    # CSV from Christina
    countries = pd.read_csv("htmlcontent/statistics/data/countries_codes_and_coordinates.csv")
    for column in countries.columns[1:]:
        countries[column] = [c.strip().replace('"', "") for c in countries[column]]
    countries['Country'] = countries['Country'].replace('Jersey','Bailiwick of Jersey') # Getting confused with New Jersey
    return countries


def get_states(state_path="htmlcontent/statistics/data/states.csv"):
    """
    Function to read in the csv file containing US state names, postal codes, and lat/long coordinates

    Parameters
    ----------------
    state_path (optional): File path to the csv file

    Returns
    ------------
    states: Pandas dataframe with state information
    """
    states = (
        pd.read_csv(state_path)
        .sort_values("State")
        .reset_index(drop=True)
    )
    return states


###################################################################
#                Interactive journal count Plot
###################################################################


def get_articles(tpub_results):
    """
    Makes a plot of the number of refereed papers over time, broken up by tpub category.
    This plot is restricted to entries that are journal articles (vs book chapter, eptrints, conference proceeding, etc)
    Parameters
    -----------
    tpub_results: TESS entries in the tpub database (from get_tpub())

    Returns
    --------
    article: Only TESS tpub entries that are from journal articles
    """
    is_article = [
        json.loads(tpub_results["metrics"][x])["doctype"] == "article"
        for x in range(len(tpub_results))
    ]
    article = tpub_results[is_article]
    article["month"] = pd.to_datetime(article["month"], format="%Y-%m", errors="coerce")
    return article


def make_interactive_paper_plot(
    article, 
    html_path="htmlcontent/statistics/images/",
    image_path="content/images/statistics/"
):
    """
    Function to make an interactive plot that shows the number of journal publications for TESS

    Parameters
    ----------------
    article: TESS tpub articles (from get_articles())
    plot_path (optional): File path to save the html plot

    Returns
    ------------
    None
    """

    start_date = pd.to_datetime('2018-04-01 00:00:00', format="%Y-%m-%d %H:%M:%S", errors='coerce') #datetime(2018, 4, 1)  # Month of TESS launch
    end_date = max(article["month"]) # Latest article on tpub
    
    #Easy way to handle recurring events (such as in a calendar) where the number of days etc are not always the same
    months = rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date)

    labels = ["exoplanets", "astrophysics"]
    # Cumulative count of number of papers by month
    ex_count = np.zeros(int(months.count()))
    as_count = np.zeros(int(months.count()))
    for ii in range(int(months.count())):
        ex_count[ii] = len(
            article[
                (article["month"] <= months[ii]) & (article["science"] == "exoplanets")
            ]
        )
        as_count[ii] = len(
            article[
                (article["month"] <= months[ii])
                & (article["science"] == "astrophysics")
            ]
        )

    layout = go.Layout(
        title="TESS journal publications over time",
        plot_bgcolor="rgb(255,255,255)",  # set the background colour
    )

    # Interactive plot to tell you how many articles there are when you hover over the points
    fig = go.Figure(layout=layout)
    fig.add_trace(
        go.Scatter(
            x=months[:],
            y=ex_count,
            mode="lines",
            name="exoplanet",
            line=dict(color="royalblue", width=5),
            hovertemplate="Date: %{x}" + "<br>Count: %{y:.0f}" + "<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=months[:],
            y=as_count,
            mode="lines",
            name="astrophysics",
            line=dict(color="tomato", width=5),
            hovertemplate="Date: %{x}" + "<br>Count: %{y:.0f}" + "<extra></extra>",
        )
    )
    fig.update_xaxes(range=[min(months), max(months)])
    fig.add_vline(x=min(months), line_width=2, line_dash="solid", line_color="black")
    fig.update_xaxes(gridwidth=0, zeroline=True, automargin=False)
    fig.update_yaxes(
        gridwidth=1,
        gridcolor="gray",
        linecolor="black",
        zeroline=True,
        zerolinecolor="Black",
        zerolinewidth=2,
        automargin=False,
    )
    fig.update_layout(
        title="<b>TESS-related Journal Publications",
        yaxis_title="Number of articles",
        xaxis=go.layout.XAxis(tickangle=45),
        legend_title="Subject",
        legend=dict(orientation="h", yanchor="bottom", y=0.05, xanchor="right", x=1),
        font=dict(size=18, color="slategray"),
        hoverlabel=dict(
            font_size=18,
        ),
        width=1024,
        height=560,
    )

    # Save the file as an html. Include a pointer to plotly-latest.min.js.
    fig.write_html(
        html_path + "papers_over_time.html",
        include_plotlyjs="./theme/js/plotly-latest.min.js",
        default_width="100%",
        default_height="100%",
    )
    
    # Save a static figure as well to use in the swipe out
    fig.write_image(image_path+'papers_over_time.png')


###################################################################
#                    Static publication Bar Chart
###################################################################

# Makes a plot of the number of refereed papers over time, broken up by tpub category
def make_static_publication_bar_chart(results, image_path="content/images/statistics/"):
    """
    Function to make a static plot that shows the number of publications for TESS, extrapolating to the end of the current year

    Parameters
    ----------------
    results: TESS tpub articles (from get_articles())
    image_path (optional): File path to save the image

    Returns
    ------------
    None
    """
    publications = (
        results.copy()
    )  # Don't restrict this plot to entries that are journal articles (vs book chapter, eptrints, conference proceeding, etc)
    #publications["month"] = pd.to_datetime(
    #    publications["month"], format="%Y-%m", errors="coerce"
    #)

    
    start_date = pd.to_datetime('2013-01-01 00:00:00', format="%Y-%m-%d %H:%M:%S", errors='coerce')
    
    # Occasionally tpub gets a publication listed in the future which messus up this extrapolation. 
    max_date =pd.to_datetime(f"{int(max(publications['year']))+1}-01-01 00:00:00", format="%Y-%m-%d %H:%M:%S", errors='coerce')
    today = pd.to_datetime('today', format="%Y-%m-%d %H:%M:%S", errors='coerce')
    if max_date > today:
    	end_date = today 
    else:
    	end_date = max_date 

    years = rrule.rrule(rrule.YEARLY, dtstart=start_date, until=end_date + pd.offsets.DateOffset(years=1))

    # Cumulative count of number of papers by month
    journal_count = np.zeros(int(years.count()) - 1)
    for ii in range(int(years.count()) - 1):
        journal_count[ii] = len(
            publications[
                (publications["month"] < years[ii + 1])
                & (publications["month"] >= years[ii])
            ]
        )
    
    last_article_date_int = end_date.timetuple().tm_yday
    latest_pub_rate = journal_count[-1]/last_article_date_int
    extrapolation = int((365-last_article_date_int) * latest_pub_rate)

        
    fig, ax = plt.subplots(1, figsize=(12, 7))
    ax.yaxis.grid()
    plot_years = [y.year for y in years][:-1]

    ax.bar(
        plot_years,
        journal_count,
        color="royalblue",
        width=0.8,
        zorder=3,
        label="TESS",
    )
    ax.bar(
        plot_years[-1],
        extrapolation,
        width=0.8,
        color="gray",
        bottom=journal_count[-1],
        label="Expected",
        zorder=3,
    )
    ax.tick_params(axis="both", which="major", labelsize=18)
    ax.set_xticks(plot_years)
    ax.set_ylabel("Publications per year", fontsize=22)
    plt.legend(
        bbox_to_anchor=(0.3, 1.04, 0.45, 0.06),
        loc="upper left",
        mode="expand",
        borderaxespad=0,
        ncol=2,
        fontsize=20,
        framealpha=0.0,
    )
    plt.savefig(image_path + "publications_barchart.png")
    plt.close()


###################################################################
#             Static Journal-by-Subject Pie Plot
###################################################################


def make_subject_piechart(results, image_path="content/images/statistics/"):
    """
    Function to make a static pie chart that shows the subject breakdown of TESS publications (astrophysics vs exoplanets)

    Parameters
    ----------------
    results: TESS tpub articles (from get_articles())
    image_path (optional): File path to save the image

    Returns
    ------------
    None
    """
    colors = ["royalblue", "tomato"]
    explode = (0.01, 0.01)
    labels = ["exoplanets", "astrophysics"]

    # One random paper was not classified, so just kick it out.
    df = results[
        (results["science"] == "exoplanets") | (results["science"] == "astrophysics")
    ]

    fig, ax = plt.subplots(figsize=(8, 8))

    # Capture each of the return elements.
    patches, texts, pcts = ax.pie(
        df["science"].value_counts(normalize=True),
        autopct="%.0f%%",
        wedgeprops={"linewidth": 3.0, "edgecolor": "white"},
        textprops={"size": "x-large"},
        labeldistance=None,
        colors=colors,
        labels=df["science"].value_counts(normalize=True).keys(),
        startangle=60,
    )
    # Style just the percent values.
    plt.setp(pcts, color="white", fontweight="bold", fontsize=45)

    ax.legend(
        bbox_to_anchor=(0.0, 1.0, 1.0, 0.01),
        loc="upper left",
        mode="expand",
        borderaxespad=0,
        ncol=2,
        fontsize=20,
        framealpha=0.0,
    )
    plt.tight_layout()

    plt.savefig(image_path + "publications_piechart.png")
    plt.close()




###################################################################
#                     Interactive Geography plots
###################################################################

# The affiliations in the tpub files often don't contain the actual location names. Here are some common omissions I have found
# Place to put common name variations
country_override = {
    "USA": "United States",
    "UK": "United Kingdom",
    "Suisse": "Switzerland",
    "Northern Ireland": "United Kingdom",
    "Republic Of Korea": "Korea, Republic of",
    "People's Republic of China": "China",
    "Iran": "Iran, Islamic Republic of",
    "Slovak Republic": "Slovakia",
    "Polska": "Poland",
    "UAE": "United Arab Emirates",
    "México": "Mexico",
    "Türkiye": "Turkey",
}

# Some affiliations don't give the country. These are ones I found in the current archive
common_mistakes_country = {
    "Massachusetts Institute of Technology": "United States",
    "Harvard-Smithsonian": "United States",
    "Kavli": "United States",
    "Space Telescope Science Institute": "United States",
    "Stanford": "United States",
    "Vanderbilt": "United States",
    "AAVSO": "United States",
    "Caltech": "United States",
    "Moorhead": "United States",
    "Los Alamos": "United States",
    "San Diego": "United States",
    "Annnapolis": "United States",
    "Louisiana State": "United States",
    "Harper College": "United States",
    "Chicago": "United States",
    "Texas": "United States",
    "American Museum of Natural History": "United States",
    "SETI": "United States",
    "Ames": "United States",
    "Space Telescope Science Insitute": "United States",
    "Goddard": "United States",
    "University of Maryland": "United States",
    "Fisk University": "United States",
    "Budapest": "Hungary",
    "Santiago": "Chile",
    "Goettingen": "Germany",
    "Korea": "South Korea",  
    "University of Southampton": "United Kingdom",
    "University of St Andrews": "United Kingdom",
    "University of Leicester": "United Kingdom",
    "University College London": "United Kingdom",
    "University of Oxford": "United Kingdom",
    "University of Manchester": "United Kingdom",
    "Geneva": "Switzerland",
    "Zurich": "Switzerland",
    "New South Wales": "Australia",
    "Tokyo": "Japan",
    "Akdeniz University": "Turkey",
    "University of Colombo": "Sri Lanka",
    "Berlin": "Germany",
}

# Many affiliations just contain the University or organization, so this links them to the state
common_mistakes_state = {
    "Princeton": "New Jersey",
    "Goddard": "Maryland",
    "GSFC": "Maryland",
    "Noqsi": "Colorado",
    "Lowell": "Arizona",
    "Ames": "California",
    "UCB Space Sciences Lab": "California",  # Berkeley
    "Cornell": "New York",
    "Space Telescope Science Institute": "Maryland",
    "Lehigh": "Pennsylvania",
    "Vanderbilt": "Tennessee",
    "SETI Institute": "California",
    "Hawai'i": "Hawaii",
    "Mikulski": "Maryland",
    "Kitt Peak": "Arizona",
    "Adler Planetarium": "Illinois",
    "American Museum of Natural History": "New York",
    "Harvard-Smithsonian": "Massachusetts",
    "San Diego": "California",
    "Chicago": "Illinois",
    "Fisk University": "Tennessee",
    "Space Telescope Science Insitute": "Maryland",
}

# Some functions to get the demographic info
def findCountry(affil, countries, verbose=False):
    """
    Find what country a TESS author is affiliated with

    Parameters
    ----------------
    affil: string with the author affiliation
    countries: The pandas dataframe containing country information
    verbose: If a country can't be found in the author affiliation, print the affiliation to screen. TODO: UPDATE TO SAVE TO A FILE?


    Returns
    -----------
    country: String containing the country an author is affiliated with (None if no affiliation found)
    """
    
    for country in countries["Country"].values:  # for each country in the csv file
        if country.lower() in affil.lower():
            if (
                country.lower() == "oman"
            ):  # Oman comes first, so romania is getting wrongly classified.
                if "romania" in affil.lower():
                    return "Romania"
            if country.lower() == "ireland":  # Should Northern Ireland be seperate?
                if "northern ireland" in affil.lower():
                    return "United Kingdom"
            if country.lower() == "georgia":  # I expect these are really the state.
                if ("united states" in affil.lower()) | ("usa" in affil.lower()):
                    return "United States"
            return country

    for country in country_override:
        if country.lower() in affil.lower():
            return country_override[country]

    for country in common_mistakes_country:
        if country.lower() in affil.lower():
            return common_mistakes_country[country]
    # Prints out every affiliation where a country couldn't be found. I used this to identify what to put in the common_mistakes_county dictionary above
    if verbose == True:
        if affil != "-":
            print("No Country identified: %s" % affil)
    return None


def findState(affil, country, states, verbose=False):
    """
    If an author is affiliated with a US state, figure out which one

    Parameters
    ----------------
    affil: string with the author affiliation
    country: string containing the country an author is affiliated with
    states: pandas dataframe containing information about each of the US states
    verbose: If a state can't be found in the author affiliation, print the affiliation to screen. TODO: UPDATE TO SAVE TO A FILE?


    Returns
    ------------
    state: String containing the country an author is affiliated with (None if not in the US or no affiliation found)
    """
    if country:  # If a country was identified
        if (country.lower() == "united states") or (
            country.lower() == "usa"
        ):  # If that country is the US find the state
            for state in states.itertuples():
                if (state.State.lower() in affil.lower()) | (
                    state.Postal in affil
                ):  # Look for either the state name spelled out or the two-letter postal code
                    return state.State

            for state in common_mistakes_state:
                if state.lower() in affil.lower():
                    return common_mistakes_state[state]
            if verbose == True:
                if affil != "-":
                    print("No State identified: %s" % affil)

    return None


def get_latlong(country, state, countries, states):
    """
    Get the lat/long of an authors affiliation. This is just a country location unless in the US, then returns the state.

    Parameters
    ----------------
    country: string containing the country an author is affiliated with
    state: string containing the state an author is affiliated with (None if not in the US or unknown)
    countries: pandas dataframe containing information about all the the countries
    states: pandas dataframe containing information about all of the US states

    Returns
    ------------
    [lat, long]: Latitude and longitude

    """
    
    if country:
        # if self.country in country_override.keys():
        #    self.country = country_override[self.country]
        if (country.lower() == "united states") or (country.lower() == "usa"):
            if state:
                lat = states[states["State"] == state]["Latitude"].values[0]
                long = states[states["State"] == state]["Longitude"].values[0]
            else:
                lat = None
                long = None
        else:
            lat = countries[countries["Country"] == country]["Latitude"].values[0]
            long = countries[countries["Country"] == country]["Longitude"].values[0]
    else:
        lat = None
        long = None
    return [lat, long]


def get_author(paper_dict, author_number, countries, states):
    """
    returns a dictionary containing pertinent information for each author

    Parameters
    ----------------
    paper_dict: dictionary containing tpub data for a given paper, already json-unpacked (json.loads(tpub_results['metrics'][paper number])
    author_num: integer representing the position of the author of interest in the full author list
    countries: pandas dataframe containing information about all the the countries
    states: pandas dataframe containing information about all of the US states

    Returns
    -----------
    author: Dictionary containing author information, including things like year of publication, type of publication, and affiliation details
    """

    author = {"name": paper_dict["author_norm"][author_number].lower()}
    if paper_dict["author_norm"][author_number] == paper_dict["first_author_norm"]:
        author["lead_author"] = 1
    else:
        author["lead_author"] = 0

    author["bibcode"] = paper_dict["bibcode"]
    author["year"] = paper_dict["year"]
    author["science"] = paper_dict["science"]
    # There could be multiple affiliations. If so, split them up.
    # This makes the resulting affiliations, countries, states, lat, and longs a list

    aff_list = paper_dict["aff"][author_number]

    if aff_list[-1] == ";":
        aff_list = aff_list[
            :-1
        ]  # Sometimes it ends with a ; which throws off the string split
    affil_split = re.split(";", aff_list.replace("lt;", "<").replace("amp;", "&"))

    author["affiliation"] = affil_split
    author["country"] = [
        findCountry(affil, countries) for affil in affil_split
    ]  # paper_dict['aff'][author_number]
    author["state"] = [
        findState(affil_split[ii], author["country"][ii], states)
        for ii in range(len(affil_split))
    ]

    latlongs = [
        get_latlong(author["country"][ii], author["state"][ii], countries, states)
        for ii in range(len(affil_split))
    ]
    author["lat"] = [coord[0] for coord in latlongs]
    author["long"] = [coord[1] for coord in latlongs]
    return author


def make_author_list(results, country, state):

    # Make a list containing author objects
    author_list = []
    for paper_num in range(len(results["metrics"])):  # for each paper
        for author_num in range(
            len(json.loads(results["metrics"][paper_num])["author_norm"])
        ):  # for each author
            author_list.append(
                get_author(
                    json.loads(results["metrics"][paper_num]),
                    author_num,
                    country,
                    state,
                )
            )
    return author_list


def make_author_group(author_list):
    # Group these to get a new list where each item is a collection of instances of the same author
    author_groups = defaultdict(list)
    for obj in author_list:
        author_groups[obj["name"]].append(obj)
    return author_groups


def plot_American_authors(
    author_list,
    states,
    html_path="htmlcontent/statistics/images/",
    image_path="content/images/statistics/"
):
    """
    Creates an html interactive plot showing the number of unique TESS authors (from any position on the author list) affiliated with a US institution from each state

    Parameters
    ----------------
    author_list: list containing author dictionaries (from make_author_list())
    states: pandas dataframe containing information about all of the US states
    plot_path: (optional) file path to where you want the plot stored

    Returns
    ------------
    None

    """
    # Plot number of unique America-based authors (regardless of position on author list) in each state
    # Find unique authors (if they have multiple affiliations they will be counted twice)
    unique_author_df = pd.DataFrame(
        data={
            "name": [obj["name"] for obj in author_list],
            "author_flag": [obj["lead_author"] for obj in author_list],
            "country": [obj["country"][0] for obj in author_list],
            "state": [obj["state"][0] for obj in author_list],
        }
    ).drop_duplicates()

    state_counts = Counter(unique_author_df["state"])
    sc_df = pd.DataFrame(
        {"state": state_counts.keys(), "Authors": state_counts.values()}
    ).dropna()
    sc_df["State"] = [
        states[states["State"] == ss]["Postal"].values[0] for ss in sc_df["state"]
    ]

    fig = px.choropleth(
        sc_df,
        locations="State",
        color="Authors",
        color_continuous_scale=[
            "mistyrose",
            "tomato",
            "red",
        ],  # Set the colors manually as the "reds" colorbar looked bad.
        locationmode="USA-states",
        scope="usa",
        range_color=(0, 100), #max(sc_df["Authors"])),
        title="Number of unique authors from US states",
    )

    fig.update_layout(
        title_text="<b>TESS Contributing authors by state",
        title_font_size=24,
        # title_x=0.15,
        showlegend=False,
        dragmode=False,
        hoverlabel=dict(font_size=18, bgcolor="white"),
        width=1024,
        height=700,
        coloraxis_colorbar_x=0.0,
        margin=dict(t=50, r=0, l=10),
    )
    fig.update_coloraxes(colorbar_tickfont={"size": 16})
    fig.update_coloraxes(colorbar_tickvals=[0,20,40,60,80,100])
    fig.update_coloraxes(colorbar_ticktext=["0","20","40","60","80","100+"]) 

    fig.write_html(
        html_path + "US_author_count.html",
        include_plotlyjs="./theme/js/plotly-latest.min.js",
        default_width="80vw",
        default_height="80vh",
    )
    # if you want to save out a static imge instead
    fig.write_image(image_path+"US_author_count.png", height=512, scale=10)


def plot_Global_authors(
    author_list,
    countries,
    html_path="htmlcontent/statistics/images/",
    image_path="content/images/statistics/"
):
    """
    Creates an html interactive plot showing the number of unique TESS authors (first authors only) affiliated with a US institution from each state

    Parameters
    ----------------
    author_list: list containing author dictionaries (from make_author_list())
    countries: pandas dataframe containing information about all the the countries
    plot_path: (optional) file path to where you want the plot stored

    Returns
    ------------
    None

    """
    
    # Make a plot showing where all lead authors are from
    lead_author_country = [
        obj["country"][0] for obj in author_list if obj["lead_author"] == 1
    ]
    country_counts = Counter(lead_author_country)
    cc_df = pd.DataFrame(
        {"country": country_counts.keys(), "count": country_counts.values()}
    ).dropna()
    cc_df["count_normalized"] = cc_df["count"] / sum(cc_df["count"])
    #import pdb;pdb.set_trace()

    fig = px.choropleth(
        cc_df,
        locations="country",
        color="count",
        color_continuous_scale=[
            "skyblue",
            "royalblue",
            "mediumblue",
        ],  # Custom color scale as the "Blues" colorbar didn't go with the theme
        locationmode="country names",
        scope="world",
        range_color=(0, 100), # max(cc_df["count"])),
        title="Lead author affiliation",
        height=600,
        width=1024,
    )

    fig.update_layout(
        title_text="<b>TESS Lead author affiliation",
        title_font_size=24,
        # title_x=0.15,
        showlegend=False,
        dragmode=False,
        hoverlabel=dict(font_size=18, bgcolor="white"),
        margin=dict(t=40, r=0, l=10),
    )
    fig.update_coloraxes(colorbar_tickfont={"size": 16})
    fig.update_coloraxes(colorbar_tickvals=[0,20,40,60,80,100])
    fig.update_coloraxes(colorbar_ticktext=["0","20","40","60","80","100+"])
    
    fig.write_html(
        html_path + "Lead_author_affiliation.html",
        include_plotlyjs="./theme/js/plotly-latest.min.js",
        default_width="80vw",
        default_height="80vh",
    )
    # Iif you want to save a static image of the plot
    fig.write_image(image_path+"Lead_author_affiliations.png", width=1024, scale=10)


###################################################################
#                  Author connection "flight map"
###################################################################


# Kind of redundant to what was done in make_author_list, but it made sorting the data for this a lot easier
def make_paper_list(results, countries, states):
    paper_list = []
    for paper_num in range(len(results["metrics"])):  # for each paper
        paper_list.append(
            [
                get_author(
                    json.loads(results["metrics"][paper_num]), ii, countries, states
                )
                for ii in range(
                    len(json.loads(results["metrics"][paper_num])["author_norm"])
                )
            ]
        )
    return paper_list


def plot_author_connections(paper_list, countries, image_path="content/images/statistics/"):
    """
    Creates a static world map with a line connecting the affiliated location of the first author with all of their collaborating authors.

    Parameters
    ----------------
    paper_list: list containing author dictionaries grouped by paper (from make_paper_list())
    countries: pandas dataframe containing information about all the the countries
    image_path: (optional) file path to where you want the plot stored

    Returns
    ------------
    None
    """
    
    fig = go.Figure()

    fig.add_trace(
        go.Scattergeo(
            locationmode="country names",
            lon=countries["Longitude"],
            lat=countries["Latitude"],
            hoverinfo="text",
            text=countries["Country"],
            mode="markers",
            marker=dict(
                size=2,
                color="rgb(220, 220, 220)",
                line=dict(width=3, color="rgba(68, 68, 68, 0)"),
            ),
        )
    )

    flight_paths = []
    for paper_num in range(len(paper_list)):
        objs = paper_list[paper_num]
        paper_country = [
            x["country"][0] for x in objs
        ]  # Note this only takes the primary affiliation
        paper_state = [x["state"][0] for x in objs]
        # if paper_country.count('United States') == 0:

        for i in range(len(objs) - 1):
            if (objs[0]["long"][0] != None) & (
                objs[i + 1]["long"][0] != None
            ):  # If there is an author affiliation
                if (
                    objs[0]["long"][0] != objs[i + 1]["long"][0]
                ):  # if the connected author is from a different institution
                    fig.add_trace(
                        go.Scattergeo(
                            # locationmode = 'country names',
                            lon=[objs[0]["long"][0], objs[i + 1]["long"][0]],
                            lat=[objs[0]["lat"][0], objs[i + 1]["lat"][0]],
                            mode="lines",
                            line=dict(width=1, color="royalblue"),
                            opacity=0.02,
                        )
                    )

    fig.update_layout(
        title_text="<b>Author connections",
        title_font_size=24,
        showlegend=False,
        width=1024,
        height=600,
        geo=dict(
            scope="world",
            projection_type="natural earth",  #'mollweide',
            showland=True,
            landcolor="rgb(243, 243, 243)",
            countrycolor="rgb(204, 204, 204)",
        ),
        hoverlabel=dict(font_size=18, bgcolor="white"),
        dragmode=False,
        margin=dict(t=50, r=50, l=10),
    )
    # This worked a lot better as a static image. The interactive plot was way too messy.
    fig.write_image(image_path + "author_connections.png", width=1024)


def main():
    results = get_tpub()
    countries = get_countries()
    states = get_states()
    article = get_articles(results)

    author_list = make_author_list(results, countries, states)
    author_groups = make_author_group(author_list)
    paper_list = make_paper_list(results, countries, states)

    # Static plots
    make_static_publication_bar_chart(article)
    make_subject_piechart(results)
    #make_wordcloud(results)
    plot_author_connections(paper_list, countries)

    # interactive plots
    make_interactive_paper_plot(article)
    plot_American_authors(author_list, states)
    plot_Global_authors(author_list, countries)

if __name__ == "__main__":
    main()
