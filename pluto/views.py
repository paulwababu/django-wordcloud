from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, HttpResponseRedirect
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import contractions
import re

# Create your views here.
