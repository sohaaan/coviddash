# Import required packages
import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
import json
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots

# Read the airline data into pandas dataframe
# airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
#                             encoding = "ISO-8859-1",
#                             dtype={'Div1Airport': str, 'Div1TailNum': str,
#                                    'Div2Airport': str, 'Div2TailNum': str})

with open('bd_zila.json') as data_file:
    bdjson = json.load(data_file)
bd_zilas = {'District2': ['Bagerhat', 'Bandarban', 'Barguna', 'Barisal', 'Bhola', 'Bogra', 'Brahamanbaria', 'Chandpur',
                         'Chittagong', 'Chuadanga', 'Comilla', 'CoxsBazar', 'Dhaka', 'Dinajpur', 'Faridpur', 'Feni',
                         'Gaibandha', 'Gazipur', 'Gopalganj', 'Habiganj', 'Jamalpur', 'Jessore', 'Jhalokati',
                         'Jhenaidah', 'Joypurhat', 'Khagrachhari', 'Khulna', 'Kishoreganj', 'Kurigram', 'Kushtia',
                         'Lakshmipur', 'Lalmonirhat', 'Madaripur', 'Magura', 'Manikganj', 'Maulvibazar', 'Meherpur',
                         'Munshiganj', 'Mymensingh', 'Naogaon', 'Narail', 'Narayanganj', 'Narsingdi', 'Natore',
                         'Nawabganj', 'Netrakona', 'Nilphamari', 'Noakhali', 'Pabna', 'Panchagarh', 'Patuakhali',
                         'Pirojpur', 'Rajbari', 'Rajshahi', 'Rangamati', 'Rangpur', 'Satkhira', 'Shariatpur', 'Sherpur',
                         'Sirajganj', 'Sunamganj', 'Sylhet', 'Tangail', 'Thakurgaon']}



# Create DataFrame
rf = pd.DataFrame(bd_zilas)
dfm= pd.read_csv('bgd_cov19.csv')
dfm= pd.concat([dfm, rf], axis=1)
dfp = pd.read_csv('Covid_All.csv')
dfm2= pd.read_csv('covid_testcenters.csv')
dfv= pd.read_csv('vaccine_bd.csv')

# Create a dash application
app = dash.Dash(__name__)
#server= app.server
# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
years=['Last 60 days','All','2020','2021']
years2=['Last 60 days','All','2021']

def datamaker(year):
  if year=='2020':
    mask = (dfp['Date'] >= '2020-03-08') & (dfp['Date'] <= '2020-12-31')
    df=dfp.loc[mask]
  elif year== '2021':
    mask = (dfp['Date'] >= '2021-01-01') & (dfp['Date'] <= '2021-12-17')
    df=dfp.loc[mask]
  elif year== 'Last 60 days':
    df = dfp.iloc[-60:, :]
  else:
    df=dfp
  return df

def datamaker2(year):
  if year== '2021':
    mask = (dfv['date'] >= '2021-01-26') & (dfv['date'] <= '2021-12-17')
    df=dfv.loc[mask]
  elif year== 'Last 60 days':
    df = dfv.iloc[-60:, :]
  else:
    df=dfv
  return df

app.layout = html.Div(children=[html.H1('Bangladesh Covid-19 Dashboard',
                                style={'textAlign': 'center',
                                'color': '#503D36',
                                'font-size': 30}),
                                        html.Div([
                                                html.P("Select Timeline"),
                                        dcc.RadioItems(
                                                id='timeline5',
                                                options=[{'value': x, 'label': x}
                                                         for x in years],
                                                value=years[0],
                                                labelStyle={'display': 'inline-block',
                                                            'padding': '3px',
                                                            'font-size': '20px',
                                                            }
                                            ),], style={'display': 'inline-block'}),

                                        html.Div([
                                                dcc.Graph(id='fig5'),
                                                ]),
                                        html.Div([
                                                html.P("Select Timeline"),
                                        dcc.RadioItems(
                                                id='timeline1',
                                                options=[{'value': x, 'label': x}
                                                         for x in years],
                                                value=years[0],
                                                labelStyle={'display': 'inline-block',
                                                            'padding': '3px',
                                                            'font-size': '20px',
                                                            }
                                            ),], style={'display': 'inline-block'}),

                                        html.Div([
                                                dcc.Graph(id='fig1'),
                                                ]),
                                        html.Div([
                                                html.P("Select Timeline"),
                                        dcc.RadioItems(
                                                id='timeline2',
                                                options=[{'value': x, 'label': x}
                                                         for x in years],
                                                value=years[0],
                                                labelStyle={'display': 'inline-block',
                                                            'padding': '3px',
                                                            'font-size': '20px',
                                                            }
                                            ),], style={'display': 'inline-block'}),
                                                html.Div([
                                                dcc.Graph(id='fig2'),
                                                ]),
                                        html.Div([
                                                html.P("Select Timeline"),
                                        dcc.RadioItems(
                                                id='timeline3',
                                                options=[{'value': x, 'label': x}
                                                         for x in years],
                                                value=years[0],
                                                labelStyle={'display': 'inline-block',
                                                            'padding': '3px',
                                                            'font-size': '20px',
                                                            }
                                            ),], style={'display': 'inline-block'}),
                                                html.Div([
                                                dcc.Graph(id='fig6'),
                                                dcc.Graph(id='fig7')
                                                ], style={'display': 'flex'}),
                                        html.Div([
                                                html.P("Select Timeline"),
                                        dcc.RadioItems(
                                                id='timeline4',
                                                options=[{'value': x, 'label': x}
                                                         for x in years2],
                                                value=years2[0],
                                                labelStyle={'display': 'inline-block',
                                                            'padding': '3px',
                                                            'font-size': '20px',
                                                            }
                                            ),], style={'display': 'inline-block'}),
                                                html.Div([
                                                dcc.Graph(id='fig8'),
                                                ], style={}),
                                        html.Div([
                                                html.P("Select Timeline"),
                                        dcc.RadioItems(
                                                id='timeline6',
                                                options=[{'value': x, 'label': x}
                                                         for x in years2],
                                                value=years2[0],
                                                labelStyle={'display': 'inline-block',
                                                            'padding': '3px',
                                                            'font-size': '20px',
                                                            }
                                            ),], style={'display': 'inline-block'}),
                                                html.Div([
                                                dcc.Graph(id='fig9'),
                                                ], style={}),
                                        html.Br(),
                                        html.Br(),
                                        html.Div([
                                                dcc.Graph(id='fig'),
                                                dcc.Graph(id='fig4')
                                                ], style={'display': 'flex'})

                    ])
@app.callback([
        Output("fig5", "figure"),
        Output("fig1", "figure"),
        Output("fig2", "figure"),
        Output("fig6", "figure"),
        Output("fig7", "figure"),
        Output("fig8", "figure"),
        Output("fig9", "figure"),
        Output("fig", "figure"),
        Output("fig4", "figure")],
        [Input("timeline5", "value"),
         Input("timeline1", "value"),
         Input("timeline2", "value"),
         Input("timeline3", "value"),
         Input("timeline4", "value"),
         Input("timeline6", "value")])

def display(timeline5,timeline1,timeline2,timeline3,timeline4,timeline6):
    fig = px.choropleth_mapbox(
        dfm,
        geojson=bdjson,
        featureidkey='properties.ADM2_EN',
        locations='District2',
        color='Total Case',
        mapbox_style="open-street-map",
        center={"lat": 23.78841, "lon": 90.34397},
        zoom=5.3,
        height=400,
        color_continuous_scale='Oryel',
        title = 'District Wise Infected Number'
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 20, "t": 30, "l": 50, "b": 10})




    fig4 = px.scatter_mapbox(dfm2, lat="Latitude", lon="Longitude", title='Sample Collection Kiosk Location',
                             color_discrete_sequence=["fuchsia"], zoom=5.3,height=400,hover_name="Address")
    fig4.update_layout(mapbox_style="open-street-map",xaxis_title='Month')
    fig4.update_layout(margin={"r": 20, "t": 30, "l": 50, "b": 10})




    df1= datamaker(timeline1)
    df2= datamaker(timeline2)
    df3 = datamaker(timeline5)
    df4 = datamaker(timeline3)
    df5 = datamaker2(timeline4)
    df6 = datamaker2(timeline6)



    fig1 = make_subplots(specs=[[{"secondary_y": True}]])
    # Create and style traces
    fig1.add_trace(go.Bar(x=df1['Date'], y=df1['New deaths'], name='New Deaths',
                         marker_color='#E04B65'  # dash options include 'dash', 'dot', and 'dashdot'
                         ), secondary_y=False)
    fig1.add_trace(go.Scatter(x=df1['Date'], y=df1['Total death rate'], name='Death Rate', mode='lines+markers',
                             line=dict(color='#347794', width=2)), secondary_y=True)

    # Edit the layout
    fig1.update_layout(title='Death Number and Percentage',
                       legend=dict(
                           orientation="h",
                           yanchor="bottom",
                           y=-0.15,
                           xanchor="right",
                           x=.95))
    fig1.update_layout(margin={"r": 0, "t": 60, "l": 60, "b": 50})




    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    # Create and style traces
    fig2.add_trace(go.Bar(x=df2['Date'], y=df2['New tested'], name='New Tested',
                              marker_color='#DB831F'))
    fig2.add_trace(go.Bar(x=df2['Date'], y=df2['New cases'], name='New Cases',
                              marker_color='#8F1B37'))
    fig2.add_trace(go.Scatter(x=df3['Date'], y=df3['Daily positive rate'], name='Positive Rate', mode='lines+markers',
                              text=df3['New deaths'],
                              line=dict(color='#56946B', width=3,
                                        )  # dash options include 'dash', 'dot', and 'dashdot'
                              ), secondary_y=True)
    # Edit the layout
    fig2.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.15,
    xanchor="right",
    x=.95),title='New Cases Scenario',
        )
    fig2.update_layout(margin={"r": 0, "t": 60, "l": 60, "b": 50})




    fig5 = make_subplots(specs=[[{"secondary_y": True}]])
    # Create and style traces
    fig5.add_trace(go.Bar(x=df3['Date'], y=df3['New cases'], name='New Cases',
                              marker_color='#516494',),secondary_y=False)
    fig5.add_trace(go.Scatter(x=df3['Date'], y=df3['Daily death rate'], name='Death Rate', mode='lines+markers',text=df3['New deaths'],
                              line=dict(color='#E04D34', width=3,
                                        )  # dash options include 'dash', 'dot', and 'dashdot'
                              ),secondary_y=True)
    fig5.add_trace(go.Scatter(x=df3['Date'], y=df3['Daily positive rate'], name='Positive Rate', mode='lines+markers',
                              text=df3['New deaths'],
                              line=dict(color='#A5E01C', width=3,
                                        )  # dash options include 'dash', 'dot', and 'dashdot'
                              ), secondary_y=True)
    fig5.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.15,
    xanchor="right",
    x=.95),title_text='Covid19 Everyday Cases Scenario'
                    )
    fig5.update_layout(margin={"r": 0, "t": 60, "l": 60, "b": 50})




    fig6 = make_subplots(specs=[[{"secondary_y": True}]])
    # Create and style traces
    fig6.add_trace(go.Scatter(x=df4['Date'], y=df4['Daily death rate'], name='Daily Death Rate',mode='lines+markers',
                             line=dict(color='#CA65E0', width=2,
                                       )  # dash options include 'dash', 'dot', and 'dashdot'
                             ), secondary_y=False)
    fig6.add_trace(go.Scatter(x=df4['Date'], y=df4['Total death rate'], name='Total Death Rate',mode='lines+markers',
                             line=dict(color='#ADE065', width=2)),secondary_y=True)

    # Edit the layout
    fig6.update_layout(title='Death Percentage Difference',
                       yaxis_title='Rate',
                      legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.2,
    xanchor="right",
    x=.95))
    fig6.update_layout(margin={"r": 20, "t": 80, "l": 50, "b": 10})




    fig7 = make_subplots(specs=[[{"secondary_y": True}]])
    # Create and style traces

    fig7.add_trace(go.Scatter(x=df4['Date'], y=df4['Daily positive rate'], name='Daily Positive Rate',mode='lines+markers',
                             line=dict(color='#E08C65', width=2)),secondary_y=False)
    fig7.add_trace(go.Scatter(x=df4['Date'], y=df4['Total positive rate'], name='Total Positive Rate',mode='lines+markers',
                             line=dict(color='#65E0D4', width=2)),secondary_y=True)
    # Edit the layout
    fig7.update_layout(title='Positive Percentage Difference',
                      yaxis_title='Rate',legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.2,
    xanchor="right",
    x=.95))
    fig7.update_layout(margin={"r": 20, "t": 80, "l": 50, "b": 10})



    fig8 = make_subplots(specs=[[{"secondary_y": True}]])
    # Create and style traces
    fig8.add_trace(go.Bar(x=df5['date'], y=df5['daily_vaccinations'], name='Daily Vaccinations',
                          marker_color='#54997F', ), secondary_y=False)
    fig8.add_trace(go.Scatter(x=df5['date'], y=df5['daily_people_vaccinated_per_hundred'], name='Vaccination rate(daily)',
                              mode='lines+markers',
                              line=dict(color='#E07A65', width=3,
                                        )  # dash options include 'dash', 'dot', and 'dashdot'
                              ), secondary_y=True)
    # Edit the layout
    fig8.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.15,
    xanchor="right",
    x=.95),title_text='Daily Vaccination Number'
                       )
    fig8.update_layout(margin={"r": 0, "t": 60, "l": 60, "b": 50})



    fig9 = make_subplots(specs=[[{"secondary_y": True}]])
    # Create and style traces
    fig9.add_trace(go.Bar(x=df6['date'], y=df6['daily_vaccinations'], name='Daily Vaccinations',
                          marker_color='#94750E'))
    fig9.add_trace(go.Bar(x=df6['date'], y=df6['daily_2nd_dose'], name='Daily 2nd Dose',
                          marker_color='#6A5AE0'))

    # Edit the layout
    fig9.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.15,
        xanchor="right",
        x=.95), title='Daily 1st Dose vs 2nd Dose',
    )
    fig9.update_layout(margin={"r": 0, "t": 60, "l": 60, "b": 50})


    return fig5,fig1,fig2,fig6,fig7,fig8,fig9,fig,fig4
# Run the application
if __name__ == '__main__':
    app.run_server(debug= True)
