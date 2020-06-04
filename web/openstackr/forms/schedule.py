from wtforms import Form, StringField, IntegerField, TimeField, validators


class ScheduleForm(Form):
    peak_start = TimeField('Peak start', [validators.InputRequired(message='Please enter the peak start time')])
    peak_end = TimeField('Peak start', [validators.InputRequired(message='Please enter the peak end time')])
    timezone = IntegerField('Timezone', [validators.InputRequired(message='Please choose the timezone')])
    image = StringField('Image', [validators.InputRequired(message='Please select an image')])
    flavor = StringField('Flavor', [validators.InputRequired(message='Please select a flavor')])
    network = StringField('Network', [validators.InputRequired(message='Please select a network')])
    count = IntegerField('Count', [validators.InputRequired(message='Please enter the number of VMs to be created'),
                                   validators.NumberRange(min=1, message='At least 1 instance must be created by the scheduled task')])
