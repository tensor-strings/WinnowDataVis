__author__ = "David Ruddell, dlruddell@gmail.com"

import os

from flask import Flask
from wtforms import fields
from ggplot import *
from gleam import Page, panels

import pandas as pd
import numpy as np


stats = ['tpr', 'fpr', 'tp', 'fp']

statchoices = [(s, s) for s in stats]

    #'tp', 'tn', 'fp', 'fn', 'auc', 'accuracy',
     #    'sens', 'spec', 'precision']

winnowOut = pd.read_csv("DWres.csv")

class DataInput(panels.InputPanel):
    title = "Winnow Data Visualization"
    xvar = fields.SelectField(label="X axis", default="fp", choices=statchoices)
    yvar = fields.SelectField(label="Y axis", default="tp", choices=statchoices)
    linear = fields.BooleanField(label="Linear Fit")
    #smoother = fields.BooleanField(label="Smoothing Curve")

class DataPlot(panels.PlotPanel):
    height = 500
    width = 500

    def __init__(self, name, dat, ID_col):
        self.name = name
        self.dat = dat
        self.ID_col = ID_col
        panels.PlotPanel.__init__(self)

    def plot(self, inputs):
        p = ggplot(aes(x=inputs.xvar, y=inputs.yvar), data=winnowOut)
        p = p + geom_point()
        if inputs.linear:
            p = p + stat_smooth(color="red", method="lm")
        p = p + geom_point()
        return p

class WinnowGleam(Page):
    title = "Winnow Data Visualization"
    input = DataInput()
    output = DataPlot("ROC-A", winnowOut, "ROC-A")

app = Flask("WinnowGleam")
WinnowGleam.add_flask(app)
app.debug = True
app.run()