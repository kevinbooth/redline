"""
Module to help frontend make requests to the API
frontend/views/api_helper.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
import requests


class APIHelper():
    """
    Class that provides helper functions to access the api
    """
    def get_from_api(url, auth):
        """
        Sends a get requests to API_ROOT_URL/url
        @param url : string
        @param auth : string
        @return json api response
        """
        response = requests.get(API_ROOT_URL + url,
                                headers={'Authorization': 'Token ' + str(auth)}
                                )

        data = response.json()
        return data

    def post_to_api(url, auth, data=''):
        """
        Sends a post requests to API_ROOT_URL/url
        @param url : string
        @param auth : string
        @param data : json (optional)
        @return json api response
        """
        response = requests.post(API_ROOT_URL + url,
                                 headers={'Authorization': 'Token ' +
                                          str(auth)},
                                 json=data)

        data = response.json()
        return data

    def public_post_to_api(url, data=''):
        """
        Sends a post requests to API_ROOT_URL/url
        @param url : string
        @param data : json (optional)
        @return json api response
        """
        response = requests.post(API_ROOT_URL + url, json=data)
        data = response.json()
        return data

    def put_to_api(url, auth, data=''):
        """
        Sends a put requests to API_ROOT_URL/url
        @param url : string
        @param auth : string
        @param data : json (optional)
        @return json api response
        """
        response = requests.put(API_ROOT_URL + url,
                                headers={'Authorization': 'Token ' +
                                         str(auth)},
                                json=data)
        data = response.json()
        return data

    def delete_from_api(url, auth, data=''):
        """
        Sends a delete requests to API_ROOT_URL/url
        @param url : string
        @param auth : string
        @return json api response
        """
        response = requests.delete(API_ROOT_URL + url,
                                   headers={'Authorization': 'Token ' +
                                            str(auth)},
                                   json=data)
        data = response.json()
        return data
