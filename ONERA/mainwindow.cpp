#include "mainwindow.h"
#include "renderwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    length = 50;
    width = 50;
    height = 50;
    percentFillingBox = 0.6;
    numberObjectsWanted = 20;
    serverAdress = "localhost:8000";

    busy = false;
    error = false;
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
    busy = true;
    error = false;

    QString url_str = "http://";
    url_str.append(serverAdress);
    url_str.append("/process?length=");
    url_str.append(QString::number(length));
    url_str.append("&width=");
    url_str.append(QString::number(width));
    url_str.append("&height=");
    url_str.append(QString::number(height));
    url_str.append("&percentFillingBox=");
    url_str.append(QString::number(percentFillingBox));
    url_str.append("&numberObjectsWanted=");
    url_str.append(QString::number(numberObjectsWanted));

    const QUrl url = QUrl(url_str);
    const QNetworkRequest request(url);

    QNetworkAccessManager *m = new QNetworkAccessManager;
    QNetworkReply *r = m->get(request);

    connect(r, SIGNAL(error(QNetworkReply::NetworkError)), this, SLOT(serverError(QNetworkReply::NetworkError)));
    connect(r, SIGNAL(finished()), this, SLOT(processOk()));
    connect(r, SIGNAL(downloadProgress(qint64, qint64)), this, SLOT(progress(qint64, qint64) ));
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
    qDebug() << bytesReceived << "/" << bytesTotal;
}


void MainWindow::processOk()
{
    busy = false;
    if(!error)
    {
        QNetworkReply *r = qobject_cast<QNetworkReply*>(sender());
        QString response_string = r->readAll();
        QStringList response_list = response_string.split("\n");
        std::vector<Box> boxes;

        foreach (const QString &box_string, response_list) {
            if(box_string.split(",").length() == 6)
                boxes.push_back(box_string);
        }

        // Fenêtre rendu
    }
}
