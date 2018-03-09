#-------------------------------------------------
#
# Project created by QtCreator 2018-03-09T09:52:21
#
#-------------------------------------------------

QT       += core gui
QT += opengl

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = ONERA
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    box.cpp \
    vector3.cpp \
    renderwindow.cpp

HEADERS  += mainwindow.h \
    box.h \
    vector3.h \
    renderwindow.h

FORMS    += mainwindow.ui \
    renderwindow.ui
