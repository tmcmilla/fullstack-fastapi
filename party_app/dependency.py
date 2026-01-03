import os
from typing import Annotated

from fastapi import Depends
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from db import engine

_templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

def _get_templates():
  return _templates


Templates = Annotated[Jinja2Templates, Depends(_get_templates)]

def get_session():
  with Session(engine) as session:
    yield session
    
'''
def gift_update_form_partial(
    request: Request,
    templates: Templates # dependency injection
):
  return templates.TemplateResponse(
    request=request,
    name="my_template.html",
    context={"content": "some text"},
  )
'''