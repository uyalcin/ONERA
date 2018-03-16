#include "mainwindow.h"
#include "renderwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::test()
{

    RenderWindow *wdg = new RenderWindow;
    wdg->show();
}
