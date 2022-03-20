from django.db import connection
from utils.services.fetch_data import dictfetchall

class MessCostPerUserFetchService:
    @classmethod
    def __query_of_users_mess_cost(cls, mess_event_id):
        sql = f"""
            select
                menccuc.id as id,
                menccuc.user_id as user_id,
                user_info.username as user_name,
                menccuc.mess_event_id as mess_event_id,
                me.start_date as mess_start_at,
	            me.end_date as mess_end_at,
                menccuc.cost_category_id as category_id,
                cost_category.cost_category_name as cost_category_name,
                cost_category.cost_category_type as cost_category_type,
                menccuc.description as description,
                menccuc."cost" as each_cost,
                cost_per_category.total_cost as total_cost_per_category,
                total_cost.total_cost_per_user,
                total_cost_overall.total_cost
            from mess_event_n_cost_category_user_cost menccuc
            join mess_event me on
            me.id = menccuc.mess_event_id
            join (
                select
                    menccuc.user_id as user_id,
                    sum(menccuc.cost) as total_cost_per_user
                from mess_event_n_cost_category_user_cost menccuc
                where mess_event_id = {mess_event_id}
                group by
                    menccuc.user_id
            ) as total_cost on
            total_cost.user_id = menccuc.user_id
            join (
                select 
                    menccuc.mess_event_id as mess_event_id,
                    sum(menccuc.cost) as total_cost
                from mess_event_n_cost_category_user_cost menccuc
                group by menccuc.mess_event_id
            ) as total_cost_overall on
            total_cost_overall.mess_event_id = menccuc.mess_event_id
            join(
                select
                    cc.id as cost_category_id,
                    cc.name as cost_category_name,
                    cc.type as cost_category_type
                from cost_category cc 
            ) as cost_category on
            cost_category.cost_category_id = menccuc.cost_category_id
            join (
                select
                    au.id as user_id,
                    au.username as username
                from auth_user au
            ) as user_info on
            user_info.user_id = menccuc.user_id
            join (
                select
                    menccuc.mess_event_id as mess_event_id,
                    menccuc.user_id as user_id,
                    menccuc.cost_category_id as cost_category_id, 
                    sum(menccuc.cost) as total_cost
                from mess_event_n_cost_category_user_cost menccuc
                group by
                    menccuc.mess_event_id,
                    menccuc.user_id,
                    menccuc.cost_category_id
            ) as cost_per_category on
            cost_per_category.mess_event_id = menccuc.mess_event_id
            and cost_per_category.user_id = menccuc.user_id
            and cost_per_category.cost_category_id = menccuc.cost_category_id 
        """

        with connection.cursor() as cursor:
            cursor.execute(sql)
            return dictfetchall(cursor)

    @classmethod
    def __map_users_mess_cost(cls, users_mess_cost_list):
        result_dict = {}
        for data in users_mess_cost_list:
            result_dict['mess_event_id'] = data['mess_event_id']
            result_dict['mess_start_at'] = data['mess_start_at']
            result_dict['mess_end_at'] = data['mess_end_at']
            result_dict['total_cost'] = data['total_cost']
            
            if 'users' not in result_dict:
                result_dict['users'] = {}
            
            if data['user_id'] not in result_dict['users']:
                result_dict['users'][data['user_id']] = {
                    "user_id": data['user_id'],
                    "user_name": data['user_name'],
                    "all_cost": [],
                    "category_wise_cost": {},
                    "total_cost_per_user": '',
                }
            
            result_dict['users'][data['user_id']]['all_cost'].append({
                "category_id": data['category_id'],
                "category_name": data['cost_category_name'],
                "category_type": data['cost_category_type'],
                "description": data['description'],
                "cost": data['each_cost']
            })

            result_dict['users'][data['user_id']]['category_wise_cost'][data['cost_category_name']] = data['total_cost_per_category']

            result_dict['users'][data['user_id']]['total_cost_per_user'] = data['total_cost_per_user']
            
        return result_dict

    @classmethod
    def get_users_mess_cost(cls, mess_event_id):
        users_mess_cost_list = cls.__query_of_users_mess_cost(mess_event_id)
        return cls.__map_users_mess_cost(users_mess_cost_list)

