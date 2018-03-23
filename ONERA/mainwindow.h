#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QDebug>
#include <QMessageBox>
#include <QtNetwork>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

public slots:
    void test();

    void updateLength(int val);
    void updateWidth(int val);
    void updateHeight(int val);
    void updatePercentFillingBox(double val);
    void updateNumberObjectsWanted(int val);
    void updateServerAdress(QString val);

    void process();
    void testServer();

    void progress(qint64 bytesReceived, qint64 bytesTotal);
    void serverError(QNetworkReply::NetworkError);
    void pingOk();

private:
    Ui::MainWindow *ui;

    int length;
    int width;
    int height;
    double percentFillingBox;
    int numberObjectsWanted;
    QString serverAdress;

    bool busy;
    bool error;
};

#endif // MAINWINDOW_H
