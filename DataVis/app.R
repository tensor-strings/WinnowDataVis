# Title     : Winnow Visualization
# Objective : Create visualization app for winnow output
# Created by: David Ruddell, dlruddell@gmail.com or dr1236@uncw.edu
# Created on: 6/21/17

import(shiny.runApp)

import(shinydashboard)
import(shinyjs)
import(RColorBrewer)
import(ggplot2)
import(data.table)
import(Rcpp)

MINOTAUR <- function(){
    .run.MINOTAUR()
    return(invisible())
}

.run.MINOTAUR <- function(){
    syst.file <- base::system.file
    filename <- syst.file("mainserver", package = "MINOTAUR")
    shiny::runApp(filename, launch.browser = TRUE)
}