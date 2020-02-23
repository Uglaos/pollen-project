from flask import jsonify, request, render_template
from . import db
from .models import Pollen
from .schemas import PollenSchema
from . import app
import random
import datetime

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8


@app.route('/all', methods=['GET'])
def all():
    query = db.session.query(Pollen)
    params = request.args

    city = params.get('city')
    date = params.get('date')
    name = params.get('name')
    date_from = params.get('date_from')
    date_to = params.get('date_to')

    if date:
        query = query.filter_by(date=date)
    elif date_from and date_to:
        query = query.filter(date_from > date_to)
    if city:
        query = query.filter_by(city=city)

    if name:
        query = query.filter_by(name=name)

    all_pollen = query.all()

    pollen_schema = PollenSchema(many=True)
    result = pollen_schema.dump(all_pollen)
    return jsonify(result)


@app.route('/zagreb')
def zagreb():
    fig = figure(
        title='Pollen in Zagreb',
        x_axis_label='Date',
        y_axis_label='Level',
        x_axis_type='datetime',
        plot_width=600,
        plot_height=600
    )

    start_date = datetime.date.today() + datetime.timedelta(-30)
    query = """
            SELECT array_agg(date), array_agg(level), name
            FROM pollen
            WHERE city='Zagreb'
            AND date >= '%s'
            GROUP BY name
        """ % start_date
    result = db.session.execute(query).fetchall()

    for city in result:
        fig.line(
            x=city._row[0],
            y=city._row[1],
            color='#{:06x}'.format(random.randint(0, 0xFFFFFF)),
            legend_label=city._row[2],
        )

    fig.legend.location = 'top_left'

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)
