from . import ma


class PollenSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'level-text', 'level', 'city', 'date')
