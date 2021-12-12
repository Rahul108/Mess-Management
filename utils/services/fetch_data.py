from django.forms.models import model_to_dict

def dictfetchall(cursor):
    # Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def get_arr_from_string(string):
    area_str = re.sub(" +", " ", string.strip())
    area_arr = re.split(", | |-", area_str)

    return area_arr

def map_queryset_by_field(queryset, field, convert_to_dict=False):
    d_map = {}
    for obj in queryset:
        d_map[getattr(obj, field)] = model_to_dict(obj) if convert_to_dict else obj

    return d_map