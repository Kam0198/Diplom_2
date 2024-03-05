from data.urls import Url


class Endpoints:
    USER_REGISTRATION = '/api/auth/register'
    USER_LOGIN = '/api/auth/login'
    USER_DELETE = '/api/auth/user'
    USER_DATA_UPDATE = '/api/auth/user'
    ORDER_CREATE = '/api/orders'
    GET_ORDER_USER = '/api/orders'

    create_user_url = f"{Url.URL}{USER_REGISTRATION}"
    delete_user_url = f"{Url.URL}{USER_DELETE}"
    login_user_url = f"{Url.URL}{USER_LOGIN}"
    create_order_url = f"{Url.URL}{ORDER_CREATE}"
    get_order_url = f"{Url.URL}{GET_ORDER_USER}"

