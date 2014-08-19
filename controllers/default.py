import json
# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

def maps():
    rows=db(db.person.id>0).select(
            db.person.name,
            db.person.latitude,
            db.person.longitude)
    x0,y0=-26.1,27.1
    return dict(googlemap_key=GOOGLEMAP_KEY,x0=x0,y0=y0,rows=rows)

def add_position():    
   position = json.loads(request.post_vars.position)
   latitude = position["latitude"]
   longitude = position["longitude"]
   if auth.user!=None:
       db.user_location.insert(user_id = auth.user.id,latitude=latitude,longitude=longitude)
   #position = request.post_vars.position
   response.flash = T(str(position))
   return dict()

def nearby():
    if auth.user!=None:
        near = db(db.user_location.user_id==db.authorised.user_id).select()
    else: near=[]
    return dict(near=near)
