from django import template
register = template.Library()

# steem
from easysteem.easysteem import Oogg,EasyAccount,EasyPost

import requests

@register.filter(name="upvote")
def upvote(value, arg):# kullanıcı upvote atmış mı atmamışmı
    try:
        voters = Oogg(node = None).voters(value.user.username,value.permlink)
    except:
        return None
    if arg in voters:
        return True
    return False

@register.filter(name="percent")
def percent(value, arg):
    return int(value/100)

@register.filter(name="account")
def account(value, arg):
    ea = EasyAccount(username = str(value))
    if arg == "about":
        return ea.get_account_info()["about"]
    if arg == "location":
        return ea.get_account_info()["location"]
    if arg == "name":
        return ea.get_account_info()["name"]
    if arg == "pp":
        pp_url = ea.get_account_info()["profile_image"]
        if requests.get(pp_url).status_code == 200:
            return pp_url
        return "/static/logo/v2/48-px.png"
    if arg == "ci":
        return ea.get_account_info()["cover_image"]
    if arg == "rep":
        return ea.account_rep()
    if arg =="voting_power":
        return ea.account_voting_power()
    if arg == "balance":
        return ea.account_balance()
    if arg == "sp":
        return ea.account_sp()

@register.filter(name="json")
def json(value, arg):
    return value[arg]

@register.filter(name="post")
def post(value,arg):
    ep = EasyPost()
    if arg == "pending_payout":
        sp = 0
        sbd = 0
        for i in ep.pending_payout(username = str(value)):
            sp += i["sp"]
            sbd += i["sbd"]
            return {"sbd":round(sbd,2),"sp":round(sp,2)}
