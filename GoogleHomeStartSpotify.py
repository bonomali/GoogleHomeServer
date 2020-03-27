import argparse
import http.client as http_client
import logging
import time
import sys

import pychromecast
from pychromecast.controllers.spotify import SpotifyController
import spotify_token as st
import spotipy
