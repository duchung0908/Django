from pymodm import fields
class test():
    class Meta:
        collection_name = 'first_app'
        final = True
        ignore_unknown_fields = True

    _id = fields.ObjectIdField(primary_key=True)
    name = fields.CharField(required=True)
    address = fields.DictField(blank=True, default={})