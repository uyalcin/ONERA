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
    qDebug("test");
}

void MainWindow::updateLength(int val)
{
    length = val;
}

void MainWindow::updateWidth(int val)
{
    width = val;
}

void MainWindow::updateHeight(int val)
{
    height = val;
}

void MainWindow::updatePercentFillingBox(double val)
{
    percentFillingBox = val;
}

void MainWindow::updateNumberObjectsWanted(int val)
{
    numberObjectsWanted = val;
}

void MainWindow::updateServerAdress(QString val)
{
    serverAdress = val;
}

void MainWindow::process()
{
    QString request = "";
    request.append(serverAdress);
    request.append("/process?length=");
    request.append(QString::number(length));
    request.append("&width=");
    request.append(QString::number(width));
    request.append("&height=");
    request.append(QString::number(height));
    request.append("&percentFillingBox=");
    request.append(QString::number(percentFillingBox));
    request.append("&numberObjectsWanted=");
    request.append(QString::number(numberObjectsWanted));
    qDebug() << request;

    RenderWindow *r = new RenderWindow();
    r->show();
}

void MainWindow::testServer()
{
    QString request = "";
    request.append(serverAdress);
    request.append("/ping");
    qDebug() << request;
}
