from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms.schedule import ScheduleForm
from .util.resources import get_resource, post_resource, delete_resource
from .util.timezone import convert_to_utc
from datetime import datetime

bp = Blueprint('schedules', __name__, url_prefix='/schedules')


@bp.route('/', methods=['GET', 'POST'])
def index():
    schedules = get_resource('schedules')
    images = get_resource('images')
    flavors = get_resource('flavors')
    networks = get_resource('networks')
    timezones = [i for i in range(-12, 13)]

    form = ScheduleForm(request.form)
    if request.method == 'POST':
        if form.validate():

            peak_start_utc_time = convert_to_utc(datetime.strptime(form.peak_start.data.strftime('%H:%M'), '%H:%M'), form.timezone.data)
            peak_end_utc_time = convert_to_utc(datetime.strptime(form.peak_end.data.strftime('%H:%M'), '%H:%M'), form.timezone.data)

            data = {
                'peak_interval': {
                    'start': peak_start_utc_time.strftime('%H:%M'),
                    'end': peak_end_utc_time.strftime('%H:%M')
                },
                'server': {
                    'image': form.image.data,
                    'flavor': form.flavor.data,
                    'network': form.network.data,
                    'count': form.count.data
                }
            }

            schedule = post_resource('schedules', data)

            if schedule is None:
                flash('Something went wrong. Please try later.', 'error')
            else:
                flash('Schedule successfully created: {}'.format(schedule), 'success')
                return redirect(url_for('schedules.index'))
        else:
            flash(next(iter(form.errors.values()))[0], 'error')

    return render_template('schedules/index.html',
                           schedules=schedules, images=images, flavors=flavors, networks=networks, timezones=timezones, form=form)


@bp.route('/<string:scheduleId>')
def delete(scheduleId):
    resp = delete_resource('schedules', scheduleId)

    if resp['success']:
        flash('Schedule {} successfully removed'.format(scheduleId), 'success')
    else:
        flash('Something went wrong. Please try later. ERROR: ' + resp['text'].lower() + '.', 'error')

    return redirect(url_for('schedules.index'))
