#include "mainwindow.h"
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
}

void MainWindow::testServer()
{
    busy = true;
    error = false;

    QString url_str = "http://";
    url_str.append(serverAdress);
    url_str.append("/ping");


    const QUrl url = QUrl(url_str);
    const QNetworkRequest request(url);

    QNetworkAccessManager *m = new QNetworkAccessManager;
    QNetworkReply *r = m->get(request);

    connect(r, SIGNAL(error(QNetworkReply::NetworkError)), this, SLOT(serverError(QNetworkReply::NetworkError)));
    connect(r, SIGNAL(finished()), this, SLOT(pingOk()));
    connect(r, SIGNAL(downloadProgress(qint64, qint64)), this, SLOT(progress(qint64, qint64) ));
}

void MainWindow::serverError(QNetworkReply::NetworkError)
{
    error = true;
    QNetworkReply *r = qobject_cast<QNetworkReply*>(sender());
    QMessageBox::critical(this, "Error", "Server connection error. Please check the URL and your internet connection. <br /><br /> Code: <br /><em>" + r->errorString() + "</em>");
}

void MainWindow::pingOk()
{
    busy = false;
    if(!error)
    {
        QNetworkReply *r = qobject_cast<QNetworkReply*>(sender());
        if(QString("onera\n").compare(r->readAll()) == 0)
            QMessageBox::information(this, "Success", "Connection success.");
        else
            QMessageBox::critical(this, "Error", "The server do not work with this client. Please check the URL.");
    }
}

void MainWindow::progress(qint64 bytesReceived, qint64 bytesTotal)

{
    if (bytesTotal != -1)
    {
        /*progression->setRange(0, bytesTotal);
        progression->setValue(bytesReceived);*/
    }
}
