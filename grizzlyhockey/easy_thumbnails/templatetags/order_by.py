from django.template import Library

register = Library()

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)

@register.filter_function
def order_by_game_number(queryset, args):
    new_query_set = list()
    for q in queryset:
        try:
            new_query_set.append(q)
        except:
            pass
    queryset = sorted(new_query_set, key=lambda tup: int(tup.game_number))
    return queryset