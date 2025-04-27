import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def render_tab(df):
    #wykres słupkowy sum sprzedazy w zależności od dnia tygodnia i kanału sprzedaży
    df['day_of_week'] = df['tran_date'].dt.day_name()
    channel_sales_by_day = df.groupby(['Store_type', 'day_of_week'])['total_amt'].sum().unstack(fill_value=0)
    sorted_channel_sales_by_day = channel_sales_by_day.loc[channel_sales_by_day.sum(axis=1).sort_values(ascending=False).index]

    traces = []
    for Store_type in sorted_channel_sales_by_day.index:
        traces.append(go.Bar(
            x=sorted_channel_sales_by_day.columns,
            y=sorted_channel_sales_by_day.loc[Store_type],
            name=Store_type,
            hoverinfo='x+y',
        ))

    sales_by_day_channel_fig = go.Figure(data=traces)

    sales_by_day_channel_fig.update_layout(
        title="Sprzedaż według kanału sprzedaży i dnia tygodnia",
        xaxis_title="Dzień tygodnia",
        yaxis_title="Suma sprzedaży",
        barmode='stack'
    )

    #wykres kołowy dla rozkładu płci w zależności od kanału sprzedaży
    gender_distribution = df.groupby(['Store_type', 'Gender'])['cust_id'].count().reset_index()

    fig_gender = go.Figure()

    for gender in gender_distribution['Gender'].unique():
        gender_data = gender_distribution[gender_distribution['Gender'] == gender]
        fig_gender.add_trace(go.Bar(
            x=gender_data['Store_type'],
            y=gender_data['cust_id'],
            name=gender,
            hoverinfo='x+y',
        ))

    fig_gender.update_layout(
        title="Rozkład płci klientów w zależności od kanału sprzedaży",
        xaxis_title="Kanał sprzedaży",
        yaxis_title="Liczba klientów",
        barmode='stack'
    )

    layout = html.Div([
        html.H1('Kanały Sprzedaży', style={'text-align': 'center'}),
        html.Div([
            html.Div([
                dcc.Graph(id='sales-by-day-channel', figure=sales_by_day_channel_fig)
            ], style={'width': '100%'})
        ]),
        html.Div([
            html.Div([
                dcc.Graph(id='gender-distribution', figure=fig_gender)
            ], style={'width': '100%'})
        ]),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='Store-type-dropdown',
                    options=[{'label': Store, 'value': Store} for Store in df['Store_type'].unique()],
                    value=df['Store_type'].unique()[0]
                )
            ], style={'width': '50%'}),
        html.Div([
                dcc.Graph(id='Store-type-sales-avg')
            ], style={'width': '100%'})
        ], style={'display': 'flex'})
    ])

    return layout

