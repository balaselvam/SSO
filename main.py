from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from auth import oauth, GOOGLE_REDIRECT_URI, FACEBOOK_REDIRECT_URI

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# REQUIRED: Authlib stores OAuth state inside session
app.add_middleware(SessionMiddleware, secret_key="super-secret-session-key")

templates = Jinja2Templates(directory="templates")


# -------------------------------
#  HOME PAGE (LOGIN PAGE)
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# -------------------------------
#  GOOGLE LOGIN
# -------------------------------
@app.get("/google-login")
async def google_login(request: Request):
    redirect_uri = GOOGLE_REDIRECT_URI
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth/callback/google")
async def google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)

    return templates.TemplateResponse("home.html",
                                      {"request": request, "user": user})


# -------------------------------
#  FACEBOOK LOGIN
# -------------------------------
@app.get("/facebook-login")
async def facebook_login(request: Request):
    redirect_uri = FACEBOOK_REDIRECT_URI
    return await oauth.facebook.authorize_redirect(request, redirect_uri)


@app.get("/auth/callback/facebook")
async def facebook_callback(request: Request):
    token = await oauth.facebook.authorize_access_token(request)
    user_resp = await oauth.facebook.get(
        "me?fields=id,name,email",
        token=token
    )
    user = user_resp.json()

    return templates.TemplateResponse("home.html",
                                      {"request": request, "user": user})
