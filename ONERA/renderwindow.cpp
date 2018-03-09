#include "renderwindow.h"
#include "ui_renderwindow.h"
#include <QtOpenGL>

RenderWindow::RenderWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::RenderWindow)
{
    ui->setupUi(this);
}

RenderWindow::~RenderWindow()
{
    delete ui;
}
