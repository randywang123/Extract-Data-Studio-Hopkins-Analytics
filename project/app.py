import os
import sys
import shutil
sys.path.append('C:\\Users\\wzixu\\Desktop\\webdev\\Extract-Data-Studio-Hopkins-Analytics')
import random
import numpy as np
from scipy import stats
import pandas as pd
import nltk
from nltk.tokenize.api import StringTokenizer
from collections import defaultdict, deque
import re
import itertools
import jellyfish
from pymining import itemmining, assocrules
from functools import reduce
from PIL import Image, ImageDraw, ImageFont
from project.oracle.modules.module import Module
from project.oracle.modules.strikerate import StrikeRate
from project.oracle.modules.obp import OBP
from project.oracle.modules.leadrunnerthird import LeadRunnerOnThird
from project.oracle.modules.leadrunnersecond import LeadRunnerOnSecond
from project.oracle.modules.leadrunnerfirst import LeadRunnerOnFirst
from project.oracle.modules.steal import Steal
from project.oracle.modules.bunt import Bunt
from project.oracle.modules.swing import Swing
from project.oracle.modules.fpt import FPT
from project.oracle.modules.fps import FPS
from project.oracle.modules.power_sequence import PowerSequence
from project.oracle.modules.zones import ClassifyZones
from project.oracle.modules.flashcard import Flashcard
from project.oracle.recommendations.recommendation import Recommendation, RecommendationItem
from project.oracle.dknowledge import Config as baseballConfig
from engine import Oracle


from flask import *



app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def mainpage():
    # form = cgi.FieldStorage()
    # data = form.getvalue('data')
    # print(data)
    if request.method == "POST":
        question = request.form["question"]
        desc_filename = os.path.join(os.getcwd(), '2017_updated_final.csv')
        config = baseballConfig(desc_filename)
        oracle = Oracle(config)
        result, sample_size, data, plot_type, rterms = oracle.run(question)

        # move the file to the directory to implement the idea
        sorce = "C:\\Users\\wzixu\\Desktop\\webdev\\Extract-Data-Studio-Hopkins-Analytics\\project\\flashcard_image.png"
        dest = "C:\\Users\\wzixu\\Desktop\\webdev\\Extract-Data-Studio-Hopkins-Analytics\\project\\static\\flashcard_image.png"
        shutil.move(sorce,dest)
        # print(result)
        # engine.main()

        return redirect(url_for("showresult"))
    else:
        return render_template("mainpage.html")

@app.route('/result')
def showresult():
    return render_template("result.html")


if __name__ == '__main__':
    app.run(debug=True)
